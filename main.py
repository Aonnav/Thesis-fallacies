import openai
import pandas
import time
from sklearn.metrics import confusion_matrix, classification_report

openai.api_key = "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"

df = pandas.read_csv(r'D:\Documents\Uni\TW\B3\Scriptie\Stats\Scriptie\full.csv', sep = ';')

gpt_fallacy = []

def gpt3(prompt, engine='text-davinci-002', response_length=64,
         temperature=1, top_p=1, frequency_penalty=0, presence_penalty=0,
         start_text='', restart_text='', stop_seq=[]):
    response = openai.Completion.create(
        prompt=prompt + start_text,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]['text']
    new_prompt = prompt + start_text + answer + restart_text
    return answer, new_prompt

def fallacies():
    for line in range(len(df)):
        prompt = """You must be a Republican or Democrat. You are not a Democrat. Therefore, you must be a Republican.
        Logical fallacy: false dilemma
        Text:""" + df.at[line,'text']
        print(prompt)
        answer, prompt = gpt3(prompt,
                              temperature=0.3,
                              frequency_penalty=0,
                              presence_penalty=0,
                              start_text='\nLogical fallacy:',
                              restart_text='\nText: ',
                              stop_seq=['\nText:', '\n'])
        print('text:' + df.at[line,'text'])
        print('GPT-3:' + answer)
        gpt_fallacy.append(answer)
        time.sleep(2)


if __name__ == '__main__':
    fallacies()
    df['gpt_fallacy2'] = gpt_fallacy
    print(df)
    df.to_csv(r'D:\Documents\Uni\TW\B3\Scriptie\Data\FullGPT.csv')


    df = pandas.read_csv(r'D:\Documents\Uni\TW\B3\Scriptie\Stats\Scriptie\FullGPT.csv', sep=';')
    print(df)
    print(classification_report(df['fallacy'], df['gpt_adjusted']))
