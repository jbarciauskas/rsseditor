import unittest

from propertyaccessor.PropertyAccessor import PropertyAccessor

class GenericObject():
    pass

class PropertyAccessorTest(unittest.TestCase):
    def setUp(self):
        dataObj = GenericObject()
        dataObj.fizz = "buzz"
        data = { "key": "value",\
                "someDict": { "foo": "bar" },\
                "someList": ['a','b','c'],\
                "someOtherList": ['a', {"foo2":"baz"}],\
                "someObj":dataObj}
        self.classUnderTest = PropertyAccessor(data)

    def testDictAccessor(self):
        self.assertEqual(self.classUnderTest.getValue("someDict.foo"), "bar")

    def testArrayAccessor(self):
        self.assertEqual(self.classUnderTest.getValue("someList[1]"), "b")

    def testBothAccessor(self):
        self.assertEqual(self.classUnderTest.getValue("someOtherList[1].foo2"), "baz")

    def testObjectAccessor(self):
        self.assertEqual(self.classUnderTest.getValue("someObj.fizz"), "buzz")

    def testInvalidObjectAccessor(self):
        self.assertRaises(TypeError, self.classUnderTest.getValue, "someObj.test")

    def testInvalidDictAccessor(self):
        self.assertRaises(KeyError, self.classUnderTest.getValue, "someDict.test")

    def testInvalidArrayAccessor(self):
        self.assertRaises(KeyError, self.classUnderTest.getValue, "someDict[1]")

    def testDictSet(self):
        self.classUnderTest.setValue("someDict.foo", "bar2")
        self.assertEqual(self.classUnderTest.getValue("someDict.foo"), "bar2")

    def testDictSetNewKey(self):
        self.classUnderTest.setValue("someDict.newKey", "ipsum")
        self.assertEqual(self.classUnderTest.getValue("someDict.newKey"), "ipsum")

    def testWeirdDictSet(self):
        self.classUnderTest.setValue("someDict.newKey1.newKey2", "face")
        self.assertEqual(self.classUnderTest.getValue("someDict.newKey1.newKey2"), "face")

    def testExtremelyWeirdDictSet(self):
        self.classUnderTest.setValue("someDict.newKey1.newKey2.newKey3.newKey4", "cafe")
        self.assertEqual(self.classUnderTest.getValue("someDict.newKey1.newKey2.newKey3.newKey4"), "cafe")

    def testListSet(self):
        self.classUnderTest.setValue("someList[1]", "lorem")
        self.assertEqual(self.classUnderTest.getValue("someList[1]"), "lorem")

    def testObjectSet(self):
        self.classUnderTest.setValue("someObj.fizz", "newAttrVal")
        self.assertEqual(self.classUnderTest.getValue("someObj.fizz"), "newAttrVal")

    def testObjectSetBadAttribute(self):
        self.assertRaises(TypeError, self.classUnderTest.setValue, "someObj.newAttr", "attrVal")

