from scraper.wikipedia import get_article
from langchain_core.documents import Document
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from ragas.testset import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context

load_dotenv()

article_loader = get_article("Madrid")
document = Document(
    page_content=article_loader["text"],
    meta_data={"title" : article_loader[""], "page_id" : article_loader["page_id"]})

generator_llm = ChatOpenAI(model="gpt-4o-mini")
embedding_llm = OpenAIEmbeddings(model="text-embedding-3-small")

generator = TestsetGenerator(
    llm=generator_llm, 
    critic_llm=generator_llm,
    embedding_model=embedding_llm
    )

testset = generator.generate_with_langchain_docs(
    documents = [document], 
    testset_size=30,
    distributions={simple: 0.4, reasoning: 0.3, multi_context: 0.3}
    )




