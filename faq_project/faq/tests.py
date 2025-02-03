from django.test import TestCase
from .models import FAQ

class FAQModelTests(TestCase):
    def setUp(self):
        """Create an FAQ instance with manual translations."""
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="<p>Django is a web framework.</p>",
            question_hi="Django क्या है?",
            answer_hi="<p>Django एक वेब फ्रेमवर्क है।</p>",
            question_bn="Django কি?",
            answer_bn="<p>Django একটি ওয়েব ফ্রেমওয়ার্ক।</p>"
        )

    def test_faq_creation(self):
        """Test if the FAQ instance is created successfully."""
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "<p>Django is a web framework.</p>")
        self.assertIsNotNone(self.faq.id)  # Ensure the object has an ID (was saved to the database)

    def test_english_translation(self):
        """Test default English translation."""
        self.assertEqual(self.faq.get_translated_question('en'), "What is Django?")
        self.assertEqual(self.faq.get_translated_answer('en'), "<p>Django is a web framework.</p>")

    def test_hindi_translation(self):
        """Test Hindi translation retrieval."""
        self.assertEqual(self.faq.get_translated_question('hi'), "Django क्या है?")
        self.assertEqual(self.faq.get_translated_answer('hi'), "<p>Django एक वेब फ्रेमवर्क है।</p>")

    def test_bengali_translation(self):
        """Test Bengali translation retrieval."""
        self.assertEqual(self.faq.get_translated_question('bn'), "Django কি?")
        self.assertEqual(self.faq.get_translated_answer('bn'), "<p>Django একটি ওয়েব ফ্রেমওয়ার্ক।</p>")

    def test_fallback_to_english(self):
        """Test fallback to English if translation is missing."""
        self.faq.question_hi = None
        self.faq.answer_hi = None
        self.assertEqual(self.faq.get_translated_question('hi'), "What is Django?")
        self.assertEqual(self.faq.get_translated_answer('hi'), "<p>Django is a web framework.</p>")

    def test_auto_translation(self):
        """Test if translations are automatically generated during object creation."""
        new_faq = FAQ.objects.create(
            question="What is Python?",
            answer="<p>Python is a programming language.</p>"
        )
        self.assertIsNotNone(new_faq.question_hi)  # Auto-translated Hindi question
        self.assertIsNotNone(new_faq.answer_hi)  # Auto-translated Hindi answer
        self.assertIsNotNone(new_faq.question_bn)  # Auto-translated Bengali question
        self.assertIsNotNone(new_faq.answer_bn)  # Auto-translated Bengali answer
