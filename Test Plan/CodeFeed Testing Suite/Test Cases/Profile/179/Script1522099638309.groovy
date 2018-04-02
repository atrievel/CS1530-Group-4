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

WebUI.setText(findTestObject('AlbertObjFolder/ProfileEdit/input_username (1)'), 'username')

WebUI.setText(findTestObject('AlbertObjFolder/ProfileEdit/input_password (1)'), 'password')

WebUI.sendKeys(findTestObject('AlbertObjFolder/ProfileEdit/input_password (1)'), Keys.chord(Keys.ENTER))

WebUI.click(findTestObject('AlbertObjFolder/ProfileEdit/button_Edit Profile (1)'))

WebUI.setText(findTestObject('AlbertObjFolder/ProfileEdit/input_txtName (1)'), 'carl')

WebUI.setText(findTestObject('AlbertObjFolder/ProfileEdit/input_txtEmail (1)'), 'email@address.com')

WebUI.setText(findTestObject('AlbertObjFolder/ProfileEdit/input_txtPass1 (1)'), 'password1')

WebUI.setText(findTestObject('AlbertObjFolder/ProfileEdit/input_txtPass2 (1)'), 'password1')

WebUI.setText(findTestObject('AlbertObjFolder/ProfileEdit/textarea_txtBio (1)'), 'hi')

WebUI.click(findTestObject('AlbertObjFolder/ProfileEdit/button_Update Profile (1)'))

WebUI.click(findTestObject('AlbertObjFolder/ProfileEdit/button_OK'))

WebUI.closeBrowser()

