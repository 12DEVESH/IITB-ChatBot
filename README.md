# IITB Q&A Chatbot: SmartBot

**Authors:**  
- Shivansh Gupta (21d070067@iitb.ac.in)  
- Dhatri Mehta (210070027@iitb.ac.in)  
- Devesh Soni (21d070025@iitb.ac.in)  

## Project Overview  
College websites are often cluttered, making information retrieval difficult, especially during critical periods like admissions. Our solution, **SmartBot**, is a conversational AI chatbot designed specifically for IIT Bombay. It simplifies access to college-related information by understanding user queries and retrieving relevant information directly from web resources.

This project is part of the course **EE782 - Advanced Topics in Machine Learning** and demonstrates our understanding of conversational AI and deep learning methodologies.

---

## Features  
- **Conversational AI**: Handles queries naturally without requiring specific formats.  
- **Web Scraping**: Extracts information from IITB websites like Gymkhana and SMP using tools like BeautifulSoup and Requests.  
- **Pretrained LLMs**: Employs Meta's Llama-2-13B model fine-tuned for robust and context-aware responses.  
- **Efficient Embedding**: Utilizes instruction-finetuned embeddings for improved language understanding.  
- **GPTQ Quantization**: Ensures efficient and high-quality performance through advanced quantization techniques.

---

## How It Works  
1. **Data Collection**: Web scraping gathers relevant information from target websites.  
2. **Preprocessing**: Data is cleaned and structured for compatibility with AI models.  
3. **Language Modeling**: Integrates Llama-2-13B for generating human-like responses.  
4. **Embedding Layer**: Enhances comprehension of user queries and context through optimized embeddings.  
5. **Response Generation**: Dynamically generates responses using advanced prompt engineering and streaming techniques.

---

## Challenges Addressed  
- **Dynamic Website Structures**: Adapted to varied HTML structures across websites.  
- **Data Consistency**: Ensured structured and error-free data for improved chatbot performance.  
- **Response Latency**: Optimized output speed through model tuning and chunk size adjustments.  
- **Evaluation Metrics**: Developed a custom evaluation metric focusing on relevance, coherence, and grammatical correctness.

---

## Results  
### Sample Interaction:  
**User:** What is SMP?  
**Bot:** SMP stands for Student Mentor Programme, a program within IIT Bombay that aims to provide constructive and positive interaction, guidance, and mentorship to junior students by senior students.  

For more examples, refer to the [Colab Notebook](link-to-colab-notebook).

---

## Technical Details  
### Key Tools and Libraries  
- **Hugging Face Transformers**  
- **BeautifulSoup and Requests** (Web scraping)  
- **PyPDFDirectoryLoader** (PDF handling)  
- **TextStreamer** (Streaming text generation)

### Comparison of Models  
| Model        | Parameters | Features  | Speed  | Human Feedback |
|--------------|------------|-----------|--------|----------------|
| Zephyr 7B    | 7B         | DPO       | 5 min  | Vague          |
| Falcon 7B    | 7B         | FA        | 30 min | Vague          |
| Mistral 7B   | 7B         | SWA       | 30 sec | Good (~50%)    |
| **Llama2 13B** | 13B       | GPTQ      | 10 sec | Good (~70%)    |

---

## Future Prospects  
- Integrating more datasets for broader coverage.  
- Enhancing multilingual capabilities.  
- Refining the evaluation metrics for automated feedback.

---

## References  
- [HuggingFace Llama-2-13B](https://huggingface.co/TheBloke/Llama-2-13B-chat-GPTQ)  
- [Instructor-Large Model](https://huggingface.co/hkunlp/instructor-large)  
- [Blog on Prompt Engineering](https://www.mlexpert.io/prompt-engineering/private-gpt4all#create-chain)  
- [Erasmus AI Chatbot Research](https://www.researchgate.net/publication/329442419_Erasmus-AI_Chatbot)  

