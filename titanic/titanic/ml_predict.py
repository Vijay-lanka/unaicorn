def pred_model(Pclass,Age,SibSp,parch,Fare):
    import pickle
    x = [[Pclass,Age,SibSp,parch,Fare]]
    randomforest = pickle.load(open('titanic_model.sav','rb'))
    predictions = randomforest.predict(x)
    if predictions == 0:
        predictions = "not survived"
    else :
        predictions = "survived"
    return predictions
