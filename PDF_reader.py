import timeit
import argparse
from rag.pipeline import build_rag_pipeline
import json
from ingest import run_ingest


def get_rag_response(query, chain):
    response = chain({'query': query})

    res = response['result']

    start_index = res.find('{')
    end_index = res.rfind('}')

    if start_index != -1 and end_index != -1 and end_index > start_index:
        json_fragment = res[start_index:end_index + 1]
        try:
            # Convert the extracted string to JSON
            json_data = json.loads(json_fragment)
            return json_data
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
    else:
        print("No JSON object found in the string.")

    return res


if __name__ == "__main__":

    Press_kit = input("Provide the path to the directory of Press kit \n")

    if Press_kit == "":
        Press_kit ="E:\\AI_project\\Python\\press_kit"
        run_ingest(Press_kit)
    else:
        run_ingest(Press_kit)


    while 1 == 1:
        """Question should follow the schema below.

        Context: {context}/Question: {question}

        i.e. Using provided press kit extract 3D Stereoscopic people, separate them by comma
        
        """
        question = input("What are you looking for?  \n")

        if question == str.lower("exit"):
            print("Closing chat")
            break
        else:
            start = timeit.default_timer()

            qa_chain = build_rag_pipeline()
            print('Retrieving answer...')
            answer = get_rag_response(question, qa_chain)

            end = timeit.default_timer()

            print(f'\nAnswer:\n {answer}')
            print('=' * 50)

            print(f"Time to retrieve answer: {end - start}")