import unittest
from dataset import translation_data
from translator import translate_text

class TestTranslator(unittest.TestCase):

    def test_translation(self):
        # Example data structure: translation_data = {"hello": {"Spanish": "hola"}}
        translation_data["hello"] = {"Spanish": "hola"}
        
        src_lang = "English"
        tgt_lang = "Spanish"
        input_text = "Hello"
        
        # Simulate the translation
        result = translate_text(input_text, src_lang, tgt_lang)
        
        self.assertEqual(result, "Hola")

    def test_translation_not_found(self):
        src_lang = "English"
        tgt_lang = "Spanish"
        input_text = "Nonexistentword"
        
        # Simulate the translation
        result = translate_text(input_text, src_lang, tgt_lang)
        
        self.assertEqual(result, "Nonexistentword")

    def test_case_preservation(self):
        translation_data["hello"] = {"Spanish": "hola"}
        
        src_lang = "English"
        tgt_lang = "Spanish"
        input_text = "HELLO"
        
        # Simulate the translation
        result = translate_text(input_text, src_lang, tgt_lang)
        
        self.assertEqual(result, "HOLA")
        
        input_text = "Hello"
        
        # Simulate the translation
        result = translate_text(input_text, src_lang, tgt_lang)
        
        self.assertEqual(result, "Hola")

if __name__ == '__main__':
    unittest.main()
