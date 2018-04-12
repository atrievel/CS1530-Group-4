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

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/a_Login (3)'))

WebUI.setText(findTestObject('AlbertObjFolder/SearchFriend/input_username (3)'), 'username')

WebUI.setText(findTestObject('AlbertObjFolder/SearchFriend/input_password (3)'), 'password')

WebUI.sendKeys(findTestObject('AlbertObjFolder/SearchFriend/input_password (3)'), Keys.chord(Keys.ENTER))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/a_Friends (3)'))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/th_Friends Since'))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/td_afriend ( justadude ) (2)'))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/th_Friends Since'))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/td_03262018'))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/th_Friends Since'))

WebUI.click(findTestObject('AlbertObjFolder/SearchFriend/td_03262018'))

WebUI.closeBrowser()
