from ConcreteHandler import ConcreteHandler

if __name__ == '__main__':
    anApplication = ConcreteHandler(None, 'anApplication')

    aSaveDialog = ConcreteHandler(anApplication, 'aSaveDialog')
    aPrintDialog = ConcreteHandler(anApplication, 'aPrintDialog')

    aPrintButton = ConcreteHandler(aPrintDialog, 'aPrintButton')
    anOKButton = ConcreteHandler(aPrintDialog, 'anOKButton')


    anOKButton.ShowHelp()
    print()
    aPrintButton.ShowHelp()
