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

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/a_Login (10)'))

WebUI.setText(findTestObject('AlbertObjFolder/AcceptanceObj/input_username (11)'), 'q')

WebUI.setText(findTestObject('AlbertObjFolder/AcceptanceObj/input_password (11)'), '23456789')

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/input_login (10)'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/a_Categories (6)'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/a_java (1)'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/span_threadUp1'))

WebUI.doubleClick(findTestObject('AlbertObjFolder/AcceptanceObj/path'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/path'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/svg_svg-inline--fa fa-arrow-do'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/path_1'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/span_2'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/path'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/span_3'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/path_1'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/span_2'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/path'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/span_threadUp1'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/svg_svg-inline--fa fa-arrow-up'))

WebUI.click(findTestObject('AlbertObjFolder/AcceptanceObj/svg_svg-inline--fa fa-arrow-up'))

WebUI.closeBrowser()

