import multiprocessing

class ConcurrentClassifier(object):
    
    def determineTrue(self, classificationFunction, dataset, threads = 4):
        classificationMapping = []
        classifiedAsTrue =[]
        with multiprocessing.Pool(threads) as pool:
            classificationMapping = list(pool.map(classificationFunction, dataset))
        for count, value in enumerate(classificationMapping):
            if(value):
                classifiedAsTrue.append(dataset[count])
        return classifiedAsTrue