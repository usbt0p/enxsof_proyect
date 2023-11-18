from abc import ABC

class Subject(ABC):
	
    observers_list = []  # Lista de observadores
    elements_list = []    # Lista de variables / atributos
    relations = {}        # Diccionario de relaciones entre ambos

    
    def addObs(self,observer):
        self.observers_list.append(observer)

    
    def removeObs(self,observer):
        self.observers_list.remove(observer)

    
    def addElem(self, element):
        self.elements_list.append(element)

    
    def removeElem(self, element):
         self.elements_list.remove(element)

    
    def getElements(self):
        return self.elements_list
    
    
    def getObservers(self):
        return self.observers_list


    
    def notify_all_observers(self):
        for observer in self.observers_list:
            observer.update(self)

    
    def notify_interested_observers(self, element):
        list_to_update = self.relations.get(element)

        for observer in list_to_update:
            observer.update()

    
    def update(self):
        pass


    
    def purge_subject(self):
        dict_to_check = dict(zip(self.elements_list, self.observers_list))

        # Initialize lists to store valid keys and values
        valid_elements = []
        valid_observers = []

        # Iterate through the keys and check if they exist in the dictionary
        for key in self.elements_list:
            if key in dict_to_check:
                valid_elements.append(key)
                valid_observers.append(dict_to_check[key])

        self.observers_list = valid_observers.copy()
        self.elements_list = valid_elements.copy()

    
    def observer_init(self, observer, topics_of_interest):
        self.addObs(observer)
        for topic in topics_of_interest:
            if topic not in self.relations.keys():
                self.addElem(topic)
                self.relations[topic] = [observer]
            else:
                self.relations[topic].append(observer)
                self.update(observer.topics_of_interest)
        