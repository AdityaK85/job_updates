import unittest
import index
import os
import io
from pypdf import PdfReader, PdfWriter


class Test(unittest.TestCase):
    def test_naukri(self):
        (status, driver) = index.naukriLogin(headless=True)
        if not status:
            print(driver.page_source)
        index.tearDown(driver)
        self.assertFalse(status)

    
    def test_update_resume(self):
        originalResumePath = index.originalResumePath
        modifiedResumePath = index.modifiedResumePath
        # Ensure the directory for the resume exists
        os.makedirs(os.path.dirname(originalResumePath), exist_ok=True)
        os.makedirs(os.path.dirname(modifiedResumePath), exist_ok=True)

        # Create a simple PDF file
        packet = io.BytesIO()
        writer = PdfWriter()
        writer.add_blank_page(width=72, height=72)
        with open(originalResumePath, "wb") as f:
            writer.write(f)

        result_path = index.UpdateResume()
        # Check if the modified PDF file is created
        self.assertTrue(os.path.exists(result_path))
        self.assertIn(modifiedResumePath, result_path)



if __name__ == "__main__":
    unittest.main()
