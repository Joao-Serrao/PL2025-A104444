import re

def process_dataset(file_path):
    with open(file_path, encoding='utf-8') as f:
        f.readline()
        lines = f.read()
    
    composers = []
    period_distribution = {}
    period_titles = {}
    
    lines = re.findall(r'([^;]*?);("([^"]|\\")*")*;\d+;([^;]*?);([^;]*?);(\d{2}:\d{2}:\d{2});(O\d+)',lines)
    for l in lines:
    	data = l
    	composers.append(data[4])
    	name = data[0]
    	name = name[1:]
    	if data[3] in period_distribution:
    		period_distribution[data[3]] += 1
    		period_titles[data[3]].append(name)
    	else:
    		period_distribution[data[3]] = 1
    		period_titles[data[3]] = [name]
    composers = sorted(composers)
    
    for key, item in period_titles.items():
    	period_titles[key] = sorted(item)
    
    with open('compositores_ordenados.txt', 'w', encoding='utf-8') as f_composers:
        for composer in composers:
            f_composers.write(composer + '\n')

    with open('distribuicao_periodo.txt', 'w', encoding='utf-8') as f_distribution:
        for period, count in period_distribution.items():
            f_distribution.write(f'{period}: {count} obras\n')

    with open('obras_por_periodo.txt', 'w', encoding='utf-8') as f_titles:
        for period, titles in period_titles.items():
            f_titles.write(f'{period}:\n')
            for title in titles:
                f_titles.write(f'  - {title}\n')
    
    return composers, period_distribution, period_titles

# Exemplo de chamada da função
file_path = 'obras.csv'  # Substitua pelo nome correto do arquivo
composers, period_distribution, period_titles = process_dataset(file_path)

print("Compositores ordenados:", composers)
print("Distribuição das obras por período:", period_distribution)
print("Obras organizadas por período:", period_titles)



