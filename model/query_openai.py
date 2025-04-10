from langchain_openai import ChatOpenAI
from langchain.schema import Document

def generate_answer_from_context(context: tuple[list[Document], str], query: str) -> str | list[str | dict]:
    # Unpack the context tuple
    documents, additional_info = context

    # Combine the page_content of all documents into a single string
    combined_context = "\n\n".join([doc.page_content for doc in documents])


    prompt = (
        f"""
          You are a Question answering legal assistant AI trained on the latest Bharatiya Nyaya Sanhita (BNS), Bharatiya Nagarik Suraksha Sanhita (BNSS),Bharatiya Sakshya Adhiniyam (BSA), which are the new Indian laws, replacing the Indian Penal Code (IPC), Code of Criminal Procedure (CrPC), and Indian Evidence Act, respectively, and came into effect on July 1, 2024. 
          You answer based ONLY on the provided context. Do not hallucinate laws or fabricate sections.
          Always quote relevant section numbers or summaries directly from the context.
          If the user is asking about Indian Penal Code, they mean Bharatiya Nyaya Sanhita.

          If the answer is not in the context, respond with:
          "I'm sorry, the information you're looking for isn't available in the current documents. Please consult the full BNS text or a legal expert."

          ----

          Context:
          {context}

          User query:
          {query}

          Answer:
        """)

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)
    response = llm.invoke(prompt)
    return response.content