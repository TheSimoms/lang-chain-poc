import argparse
import logging
import os

from dotenv import load_dotenv
from langchain.chains.question_answering import load_qa_chain
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.embeddings import GPT4AllEmbeddings
from langchain.llms import GPT4All
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma

from util.data import data_file_path


def still_spørsmål(spørsmål: str):
    load_dotenv()

    logging.debug(f'Forsøker å finne svaret på følgende spørsmål: "{spørsmål}"')
    logging.debug('Laster inn PDF-dokumenter')

    loader = PyPDFDirectoryLoader(data_file_path('pdf/'))

    logging.debug('Splitter PDF-dokumenter opp i mindre biter')

    data = loader.load_and_split(RecursiveCharacterTextSplitter(chunk_size = 500))

    logging.debug('Lager vectorstores')

    embeddings = Chroma.from_documents(documents=data, embedding=GPT4AllEmbeddings())

    logging.debug('Laster inn LLM')

    llm_navn = os.getenv('LLM', 'mistral-7b-openorca.Q4_0.gguf.gguf')

    logging.debug(f'Bruker LLM {llm_navn}')

    llm = GPT4All(model=data_file_path(f'modeller/{llm_navn}'))
    chain = load_qa_chain(llm=llm, chain_type='stuff')

    logging.debug('Utfører spørring')

    docs = embeddings.similarity_search(spørsmål)
    svar = chain.run(input_documents=docs, question=spørsmål)

    logging.debug('Spørring ferdig')

    return svar


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Still et spørsmål.')

    parser.add_argument('-d', '--debug', action='store_true')
    parser.add_argument('spørsmål')

    args = parser.parse_args()

    logging.basicConfig(encoding='utf-8', level=logging.DEBUG if args.debug else logging.WARN)

    print(still_spørsmål(args.spørsmål))
