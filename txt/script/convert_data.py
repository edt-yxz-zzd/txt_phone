

r'''
e ../../python3_src/seed/io/savefile/convert_data.py

噪声太多:
    set<frozenset<...>>:
        出现大量:frozenset({...})

cfg - config
#'''




class DataConverter:
    def __get_container_type__(sf):
        #not_a_container, ordered, unordered
        pass
    def __convert_data__(sf, data):
        pass
    pass
class DataConverter__not_a_container(DataConverter):
    pass
class DataConverter__ordered(DataConverter):
    pass
class DataTypeDescriptor:
    def __init__(sf, *args)
        sf.__args = args

    def __get_data_type__(sf, parent_config, data)->'data_type':
        pass
    def __get_data_converter__(sf, parent_config, data_type)->'DataConverter':
        pass



