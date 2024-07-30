import streamlit as st
from app.slide_generator import generate_slide_titles, generate_slide_content
from app.image_generator import generate_image
from app.presentation_builder import create_presentation
from utils.openai_helper import set_openai_api_key

def main():
    st.title("AI-Powered PowerPoint Generator")
    
    set_openai_api_key()
    
    topic = st.text_input("Enter the presentation topic:")
    num_slides = st.slider("Number of slides:", 1, 10, 5)
    template = st.selectbox("Choose a template:", ["template1.pptx", "template2.pptx", "template3.pptx"])
    
    if st.button("Generate Presentation"):
        with st.spinner("Generating presentation..."):
            try:
                prs = create_presentation(topic, num_slides, template)
                
                # Save the presentation
                prs.save("generated_presentation.pptx")
                
                st.success("Presentation generated successfully!")
                
                # Provide download link
                with open("generated_presentation.pptx", "rb") as file:
                    btn = st.download_button(
                        label="Download PowerPoint",
                        data=file,
                        file_name="generated_presentation.pptx",
                        mime="application/vnd.openxmlformats-officedocument.presentationml.presentation"
                    )
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()