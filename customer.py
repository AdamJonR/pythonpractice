import person

#
class Customer(person.Person):
    #
    def __init__(self, name, address, telephone, customer_id, is_on_mailing_list):
        #
        person.Person.__init__(self, name, address, telephone)
        #
        self.__customer_id = customer_id
        #
        self.__is_on_mailing_list = is_on_mailing_list
        
    #
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id
    
    #
    def get_customer_id(self):
        return self.__customer_id
    
    #
    def set_is_on_mailing_list(self, is_on_mailing_list):
        self.__is_on_mailing_list = is_on_mailing_list
    
    #
    def get_is_on_mailing_list(self):
        return self.__is_on_mailing_list
        