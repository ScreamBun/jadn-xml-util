import json
import os
from lxml import etree
import xml.etree.ElementTree as ET


def get_after_last_occurance(char: str, value: str):
    str_split = value.rsplit(char, 1)
    after_last = str_split[-1]
    return after_last


def safe_list_get (l, idx, default):
  try:
    return l[idx]
  except IndexError:
    return default


def get_xml_file(file_name):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    print(file_dir)
    xml_file_path = os.path.join(file_dir, './test_data/xml/' + file_name)
    xml_file_path = os.path.abspath(os.path.realpath(xml_file_path))  

    doc = etree.parse(xml_file_path)    

    return doc


def get_xsd_file(file_name):
    file_dir = os.path.dirname(os.path.realpath('__file__'))
    print(file_dir)
    xsd_file_path = os.path.join(file_dir, './test_data/xsd/' + file_name)
    xsd_file_path = os.path.abspath(os.path.realpath(xsd_file_path))   

    with open(xsd_file_path, 'r') as f:
        xmlschema_doc = etree.parse(f)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    return xmlschema


def read_file(file_name):
  with open(file_name, 'r') as f:
      data = f.read()

  return data;


def write_to_file(root: ET.Element, filename: str):
    
    # Obtain decode string by decode()
    # function
    # xml_decode = data.decode()

    # text_file = open("./out/" + filename, "w")
    # text_file.write(xml_decode)
    # text_file.close()

    # wrap it in an ElementTree instance, and save as XML
    tree = ET.ElementTree(root)
    ET.indent(tree, space="\t", level=0)

    tree.write("./out/" + filename,
              xml_declaration=True,encoding='utf-8',
              method="xml")    
    
def read_type_data_from_file(filename):

  f = open('./test_data/jadn/' + filename) 
  data = json.load(f)
 
  # for i in data['info']:
  #   print(i)

  # for i in data['types']:
  #   print(i)    
 
  f.close()

  return data['types']  