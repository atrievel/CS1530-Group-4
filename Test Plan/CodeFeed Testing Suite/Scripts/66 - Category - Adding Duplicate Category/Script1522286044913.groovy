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

WebUI.navigateToUrl('http://localhost:5000/login')

WebUI.setText(findTestObject('Category Testing/input_username (2)'), 'test')

WebUI.setText(findTestObject('Category Testing/input_password (2)'), '123456789')

WebUI.click(findTestObject('Category Testing/input_login (1)'))

WebUI.click(findTestObject('Category Testing/a_Categories (2)'))

WebUI.click(findTestObject('Category Testing/button_New category (1)'))

WebUI.setText(findTestObject('Category Testing/input_txtCategoryName (1)'), 'test66')

WebUI.setText(findTestObject('Category Testing/textarea_txtDescription (1)'), 'test66')

WebUI.click(findTestObject('Category Testing/button_Post Category (1)'))

WebUI.click(findTestObject('Category Testing/button_OK (1)'))

WebUI.refresh()

WebUI.click(findTestObject('Category Testing/button_New category (1)'))

WebUI.setText(findTestObject('Category Testing/input_txtCategoryName (1)'), 'test66')

WebUI.setText(findTestObject('Category Testing/textarea_txtDescription (1)'), 'test66')

WebUI.click(findTestObject('Category Testing/button_Post Category (1)'))

WebUI.verifyElementVisible(findTestObject('Category Testing/div_i  Oh no'))

WebUI.verifyElementPresent(findTestObject('Category Testing/div_That catgeory already exis'), 0)

WebUI.verifyElementPresent(findTestObject('Category Testing/div_i  Oh noThat catgeory alre'), 0)

WebUI.verifyElementPresent(findTestObject('Category Testing/button_OK (1)'), 0)

WebUI.closeBrowser()

