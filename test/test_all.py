import webtest

def suite():
    modules = ["test_infobase"]
    return webtest.suite(modules)

if __name__ == "__main__":
    webtest.main()
