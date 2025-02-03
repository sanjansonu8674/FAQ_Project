from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from deep_translator import GoogleTranslator
from django.utils.html import strip_tags  # To handle CKEditor HTML content

# Function to translate text
def translate_text(text, target_lang):
    try:
        if not text:
            return ""  # Handle empty text
        translator = GoogleTranslator(source='auto', target=target_lang)
        return translator.translate(text)
    except Exception as e:
        print(f"Translation failed: {e}")
        return text  # Fallback to the original text if translation fails

class FAQ(models.Model):
    question = models.TextField()
    answer = CKEditor5Field('Answer', config_name='extends')

    # Translated fields
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation
    answer_hi = CKEditor5Field('Answer (Hindi)', config_name='extends', blank=True, null=True)
    answer_bn = CKEditor5Field('Answer (Bengali)', config_name='extends', blank=True, null=True)

    # Retrieve translated text with fallback to English
    def get_translated_question(self, lang='en'):
        translated_text = getattr(self, f'question_{lang}', None)
        return translated_text if translated_text else self.question  # Fallback to English

    def get_translated_answer(self, lang='en'):
        translated_text = getattr(self, f'answer_{lang}', None)
        return translated_text if translated_text else self.answer  # Fallback to English

    # Override save method to automate translations
    def save(self, *args, **kwargs):
        if not self.question_hi:
            self.question_hi = translate_text(self.question, 'hi')
        if not self.question_bn:
            self.question_bn = translate_text(self.question, 'bn')

        # Strip HTML before translation (to avoid breaking the formatting)
        plain_answer = strip_tags(self.answer)
        if not self.answer_hi:
            translated_hi = translate_text(plain_answer, 'hi')
            self.answer_hi = f"<p>{translated_hi}</p>"  # Re-wrap in paragraph tag
        if not self.answer_bn:
            translated_bn = translate_text(plain_answer, 'bn')
            self.answer_bn = f"<p>{translated_bn}</p>"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
