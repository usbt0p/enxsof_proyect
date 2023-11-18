from abc import ABC, abstractmethod
from observer import Observer, Observable

class Subject(ABC):
	
    observers_list = []  # Lista de observadores
    elements_list = []    # Lista de variables / atributos
    relations = {}        # Diccionario de relaciones entre ambos

    @abstractmethod
    def subscribe_to(self):
        pass

    @abstractmethod
    def update(self):
        pass
    
    def addObs(self,observer:Observer) -> None:
        self.observers_list.append(observer)

    
    def removeObs(self,observer:Observer) -> None:
        self.observers_list.remove(observer)

    
    def addElem(self, element) -> None:
        self.elements_list.append(element)

    
    def removeElem(self, element) -> None:
         self.elements_list.remove(element)

    
    def getElements(self) -> list:
        return self.elements_list
    
    
    def getObservers(self) -> list:
        return self.observers_list


    
    def notify_all_observers(self) -> None:
        for observer in self.observers_list:
            observer.update(self)

    
    def notify_interested_observers(self, element) -> None:
        list_to_update = self.relations.get(element)

        for observer in list_to_update:
            observer.update()

    
    def update(self) -> None:
        pass


    
    def purge_subject(self) -> None:
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

    
    def observer_init(self, observer, topics_of_interest) -> None:
        self.addObs(observer)
        for topic in topics_of_interest:
            if topic not in self.relations.keys():
                self.addElem(topic)
                self.relations[topic] = [observer]
            else:
                self.relations[topic].append(observer)
                self.update(observer.topics_of_interest)
        