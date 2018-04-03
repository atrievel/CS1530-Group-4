import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.checkpoint.CheckpointFactory as CheckpointFactory
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as MobileBuiltInKeywords
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testcase.TestCaseFactory as TestCaseFactory
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testdata.TestDataFactory as TestDataFactory
import com.kms.katalon.core.testobject.ObjectRepository as ObjectRepository
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WSBuiltInKeywords
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUiBuiltInKeywords
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys

WebUI.openBrowser('')

WebUI.navigateToUrl('http://localhost:5000/')

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/a_Login (5)'))

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalCategories/input_username (5)'), 'rasta')

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalCategories/input_password (5)'), 'ramboman')

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/input_login (5)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/a_Categories (5)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/a_java (3)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/button_New thread (2)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/button_'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/a_hello (1)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/button_New comment (1)'))

WebUI.setText(findTestObject('AlbertObjFolder/FunctionalCategories/textarea_txtBody (1)'), 'skrrt')

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/button_Submit Comment (1)'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/div_Your new comment was creat'))

WebUI.click(findTestObject('AlbertObjFolder/FunctionalCategories/button_OK (2)'))

WebUI.closeBrowser()

