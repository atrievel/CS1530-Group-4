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

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/a_Login'))

WebUI.setText(findTestObject('AlbertObjFolder/SearchFriend/input_username'), 'username')

WebUI.setText(findTestObject('AlbertObjFolder/SearchFriend/input_password'), 'password')

WebUI.sendKeys(findTestObject('AlbertObjFolder/SearchFriend/input_password'), Keys.chord(Keys.ENTER))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/a_Friends'))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/button_Friend Requests'))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/button_Accept Request'))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/button_OK'))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/button_Done'))

WebUI.setText(findTestObject('AlbertObjFolder/SearchFriend/input_form-control form-contro'), 'pooo')

WebUI.sendKeys(findTestObject('AlbertObjFolder/SearchFriend/input_form-control form-contro'), Keys.chord(Keys.ENTER))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/td_No matching records found'))

WebUI.closeBrowser()

