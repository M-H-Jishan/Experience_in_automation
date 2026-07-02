import os
import logging
import sys

import streamlit as st
from dotenv import load_dotenv

from app.presentation_builder import create_presentation

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)],
)
logger = logging.getLogger(__name__)


def main():
    st.title("AI PowerPoint Generator")
    st.write("Generate a presentation with AI-powered slide titles, content, and images.")

    topic = st.text_input("Presentation Topic", placeholder="e.g., The Future of AI")
    num_slides = st.slider("Number of Slides", min_value=3, max_value=15, value=5)
    template = st.selectbox("Template", ["None", "default.pptx"], index=0)

    if st.button("Generate Presentation"):
        if not topic:
            st.error("Please enter a topic.")
            return

        with st.spinner("Generating presentation..."):
            try:
                template_name = None if template == "None" else template
                prs = create_presentation(topic, num_slides, template_name)

                output_path = f"generated_{topic.replace(' ', '_')}.pptx"
                prs.save(output_path)
                st.success(f"Presentation saved as {output_path}")

                with open(output_path, "rb") as f:
                    st.download_button(
                        label="Download Presentation",
                        data=f,
                        file_name=output_path,
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation",
                    )
            except ValueError as e:
                st.error(str(e))
            except Exception as e:
                logger.error(f"Error: {e}", exc_info=True)
                st.error(f"Failed to generate presentation: {e}")


if __name__ == "__main__":
    main()
