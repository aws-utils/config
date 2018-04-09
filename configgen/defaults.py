from troposphere import awslambda, iam, apigateway

def createDefaults(defaults):
    return {
        'lambda': lambdaDefaults(defaults)
    }

def lambdaDefaults(defaults):
    lamFunc = awslambda.Function("default")

    for k, v in defaults["function"].iteritems():
        try:
            setattr(lamFunc, k, v)
        except AttributeError as attrErr:
            print "Error with " + k
            print attrErr
        except Exception as e:
            print e

    return {
        'function': lamFunc
    }
