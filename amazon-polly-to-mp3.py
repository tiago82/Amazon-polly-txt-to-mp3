# by tiago8204 
# Testado no Python 3.9
# 29/out/2020
import glob
import boto3
import os
import time
from time import sleep
from platform import system as os_name
print('--------------------------\n')
print(' Amazon Polly \n')
print('--------------------------')
def main():
    try:
        count = 0
        polly_client = boto3.Session(aws_access_key_id='YOUR_ACESS_ID',
                                     aws_secret_access_key='YOUR_ACESS_KEY',
                                     region_name='us-west-2').client('polly')

        # Os arquivos devem estar na mesma pasta
        files = sorted(glob.glob(f'{os.getcwd()}/*.txt'), key=len)
        for n, file_name in enumerate(files):            
            count += 1
            NomeAquivo = file_name+".mp3"
            if os.path.exists(NomeAquivo):   
                    print("\n Não processado: arquivo já existe.\n  ", NomeAquivo)       
            else:
                with open(file_name, 'r') as file_handle:
                    print('\n Processando arquivo...\n ->', NomeAquivo)
                    text = file_handle.read()
                    response = polly_client.synthesize_speech(VoiceId='Vitoria',OutputFormat='mp3',Text=text)
                    file = open(f'{file_name}.mp3', 'wb')
                    file.write(response['AudioStream'].read())
                    file.close()

    except OSError as error:
        print('Ocorreu um erro', error)


if __name__ == "__main__":
    main()
time.sleep(1)
print('\n \n Fim do programa.\n')
time.sleep(1)

