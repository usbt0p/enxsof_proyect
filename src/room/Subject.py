from abc import ABCMeta, abstractmethod

class Subject(metaclass=ABCMeta):
	
    @abstractmethod
    def __init__(self):
        self.observers_list = []  # Lista de observadores
        self.elements_list = []    # Lista de variables / atributos
        self.relations = {}        #Diccionario de relaciones entre ambos

    @abstractmethod
    def addObs(self,observer):
        self.observers_list.append(observer)

    @abstractmethod
    def removeObs(self,observer):
        self.observers_list.remove(observer)

    @abstractmethod
    def addElem(self, element):
        self.elements_list.append(element)

    @abstractmethod
    def removeElem(self, element):
         self.elements_list.remove(element)

    @abstractmethod
    def getElements(self):
        return self.elements_list
    
    @abstractmethod
    def getObservers(self):
        return self.observers_list


    @abstractmethod
    def notify_all_observers(self):
        for observer in self.observers_list:
            observer.update(self)

    @abstractmethod
    def notify_interested_observers(self, element):
        list_to_update = self.relations.get(element)

        for observer in list_to_update:
            observer.update()

    @abstractmethod
    def update():
        


    @abstractmethod
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

    @abstractmethod
    def observer_init(self, observer):
        self.addObs(observer)
        for topic in observer.topics_of_interest:
            if topic not in self.relations.keys():
                self.addElem(topic)
                self.relations[topic] = [observer]
            else:
                self.relations[topic] = 
        
                
