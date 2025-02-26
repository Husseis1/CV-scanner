def read_file(file_name):
    try:
        with open(file_name, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return None


def find_keywords(file_content, keywords):
    found_keywords = set()
    for keyword in keywords:
        if keyword in file_content:
            found_keywords.add(keyword)


    lista=[]
    for i in range(len(keywords)):
        if keywords[i] not in found_keywords:
            lista.append(keywords[i])
    return  sorted(found_keywords),sorted(lista)


def print_results(found_keywords, not_keywords):




    print("Keywords found:")
    for keyword in found_keywords:
        print(keyword)

    print()
    print("Keywords not found:")
    for keyword in not_keywords:
        print(keyword)


def main():
    file_name = input("Enter the name of the file used.\n")
    file_content = read_file(file_name)
    if file_content is None:
        print("Error in reading the file. The program terminates.")
        return
    keyworld2 = input("Enter the keywords you want to search for, separated by commas.\n")
    keywords = [keyword.strip() for keyword in keyworld2.split(',')]
    found_keywords, not_found_kw = find_keywords(file_content, keywords)
    print_results(found_keywords, not_found_kw)
main()