from typing import List, Dict, Tuple

def get_XML_value(xml_element:'string')-> 'string':
    """
    Takes a simple XML element, with just one opening tag and one closing tag
    Returns the content
    input: <a att="whatever">content</a>
    output: content
    Returns -1 if the XML is complex
    """
    if xml_element.count('<') != 2 or xml_element.count('>') != 2:
        return -1
    initial_pos = xml_element.find('>') + 1
    final_pos = initial_pos + xml_element[initial_pos:].find('<')
    return xml_element[initial_pos:final_pos]


def parse_ib_symbol_record(html_string:'string')-> 'tuple':
    """
    Takes an string as argument
    This string contains a html page from IB website
    It is expected that the string contains 4 <td> tags
    Tag 1 is the IB Symbol
    Tag 2 is the name of the company
    Tag 3 is the Exchange symbols (which matches IB Symbom is most occasions)
    Tag 4 is the currency of the stock in the Exchange 
    The function returns a tuple: (Tag 1, Tag 2, Tag 3, Tag 4)
    """
    tag = '<td>'
    tag_final = '</td>'
    tags = []
    if html_string.count(tag) != 4:
        return -1
    for _ in range (html_string.count(tag)):
        i_index = html_string.find(tag)
        f_index = html_string.find(tag_final)
        retrieved_tag = html_string[i_index + len(tag):f_index]
        if retrieved_tag[0] == '<':
            retrieved_tag = get_XML_value(retrieved_tag)
        tags.append(retrieved_tag)
        # print(count, ': ', i_index+len(tag), f_index, html_string[i_index+len(tag):f_index])
        html_string = html_string[f_index+len(tag):]
        # print(html_string)
    return tuple(tags)
