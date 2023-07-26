import csv
import xml.etree.ElementTree as ET


def xml_to_csv(xml_file, csv_file):
    # Cria o objeto ElementTree a partir do arquivo XML
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Abre o arquivo CSV para escrita
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)

        # Escreve os cabeçalhos das colunas no arquivo CSV
        headers = []
        for child in root[0]:
            headers.append(child.tag)
        writer.writerow(headers)

        # Escreve os dados no arquivo CSV
        for element in root.findall('.//'):
            row = []
            for child in element:
                row.append(child.text)
            writer.writerow(row)


# Exemplo de uso
xml_file = 'caminho/do/arquivo.xml'
csv_file = 'caminho/do/arquivo.csv'
xml_to_csv(xml_file, csv_file)
