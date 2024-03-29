from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
import xlsxwriter
import openpyxl
import time

browser = webdriver.Chrome("C:/browserdrivers/chromedriver.exe");

browser.get('http://demo.seleniumeasy.com/');
browser.maximize_window();

mysecs = 3;

time.sleep(mysecs);

myworkbook = openpyxl.load_workbook('C:/test/test.xlsx')
mysheet = myworkbook['Sheet1']

# Open Simple Form Demo screen

InputForms = browser.find_element_by_link_text("Input Forms");
InputForms.click();
InputForms.send_keys(Keys.DOWN);

browser.find_element_by_link_text("Simple Form Demo").click();
#input1 = "This is the first input box";

input1 = "This is the first input box"
browser.find_element_by_id("user-message").send_keys(input1);
browser.find_element_by_css_selector("button.btn:nth-child(2)").click();

output1 = browser.find_element_by_id("display");
a1 = output1.text

if (input1 in output1.text):
   print("Your Input text matched");
   print("The input expected: " + input1);
   print("The input shown: " + a1);

else:
   print("Your Input text did not match");
   print("The input expected: " + input1);
   print("The input shown: " + a1);

num1 = mysheet['A1'].value
num2 = mysheet['A2'].value

sum1 = num1 + num2;
msum1 = str(sum1);
browser.find_element_by_id("sum1").send_keys(num1);
browser.find_element_by_id("sum2").send_keys(num2);

browser.find_element_by_css_selector("button.btn:nth-child(3)").click();

output2 = browser.find_element_by_id("displayvalue");

a2 = output2.text

if (msum1 in output2.text):
   print("The sum is correct");
   print("The sum expected: " + msum1);
   print("The sum calculated: " + a2);

else:
   print("The sum is not correct");
   print("The sum expected: " + msum1);
   print("The sum calculated: " + a2);

#return from Simple Form Demo to Main Page
browser.back();
time.sleep(mysecs);

#Open CheckBox Demo screen
InputForms2 = browser.find_element_by_link_text("Input Forms");
InputForms2.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Checkbox Demo").click();
#Click On Checkbox
browser.find_element_by_id("isAgeSelected").click();
# Verify expected text
input3 = "Success - Check box is checked";
output3 = browser.find_element_by_id("txtAge");

a3 = output3.text

if (input3 in output3.text):
   print("Your Input text matched");
   print("The input expected: " + input3);
   print("The input shown: " + a3);

else:
   print("Your Input text did not match");
   print("The input expected: " + input3);
   print("The input shown: " + a3);

#Uncheck the checkbox
browser.find_element_by_id("isAgeSelected").click();

#4 checkboxes test

buttonchecktext = browser.find_element_by_id("check1");
checkBox1 = browser.find_element_by_xpath("//label[contains(.,'Option 1')]");
checkBox2 = browser.find_element_by_xpath("//label[contains(.,'Option 2')]");
checkBox3 = browser.find_element_by_xpath("//label[contains(.,'Option 3')]");
checkBox4 = browser.find_element_by_xpath("//label[contains(.,'Option 4')]");

if (not(checkBox1.is_selected())) and (not(checkBox2.is_selected())) and (not(checkBox3.is_selected())) and (not(checkBox4.is_selected())):
   print("No checkboxes selected: ");
   print("The button text: " + buttonchecktext.get_attribute("value"));

if (not(checkBox1.is_selected())):
   checkBox1.click();
   print("1st checkbox is selected: ");
   print("The button text: " + buttonchecktext.get_attribute("value"));

if (not(checkBox2.is_selected())):
   checkBox2.click();
   print("1st and 2nd checkboxes selected: ");
   print("The button text: " + buttonchecktext.get_attribute("value"));

if (not(checkBox3.is_selected())):
   checkBox3.click();
   print("1st, 2nd, and 3rd checkboxes selected: ");
   print("The button text: " + buttonchecktext.get_attribute("value"));

if (not(checkBox4.is_selected())):
   checkBox4.click();
   print("1st, 2nd, 3rd, and 4th checkboxes selected: ");
   print("The button text: " + buttonchecktext.get_attribute("value"));

checkBox1.click();
print("1st checkbox is deselected: ");
print("The button text: " + buttonchecktext.get_attribute("value"));

checkBox2.click();
print("1st and 2nd checkbox deselected: ");
print("The button text: " + buttonchecktext.get_attribute("value"));

checkBox3.click();
print("1st, 2nd, and 3rd checkbox deselected: ");
print("The button text: " + buttonchecktext.get_attribute("value"));

checkBox4.click();
print("1st, 2nd, 3rd, and 4th checkbox deselected: ");
print("The button text: " + buttonchecktext.get_attribute("value"));

#return from Checkbox Demo to Main Page
browser.back();
time.sleep(mysecs);

#Open Radio Buttons Demo screen
InputForms3 = browser.find_element_by_link_text("Input Forms");
InputForms3.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Radio Buttons Demo").click();

#Verify expected text for male checkbox
out1 = mysheet['B1'].value
out2 = mysheet['B2'].value
radio1 = browser.find_element_by_xpath("(//label[@class='radio-inline'][contains(.,'Male')])[1]");
radio2 = browser.find_element_by_xpath("(//label[@class='radio-inline'][contains(.,'Female')])[1]");
checkbutton1 = browser.find_element_by_id("buttoncheck");
checkmessage = browser.find_element_by_xpath("//p[@class='radiobutton']");

radio1.click();
checkbutton1.click();

a5 = checkmessage.text

if (out1 in checkmessage.text):
	print("The output expected: " + out1);
	print("The output shown: " + a5);

else:
	print("The output expected: " + out1);
	print("The output shown: " + a5);

radio2.click();
checkbutton1.click();

a6 = checkmessage.text

if (out2 in checkmessage.text):
	print("The output expected: " + out2);
	print("The output shown: " + a6);

else:
	print("The output expected: " + out2);
	print("The output shown: " + a6);

abc1 = "Sex : Male";
abc2 = "Sex : Female";
abc3 = "Age group: 0 - 5";
abc4 = "Age group: 5 - 15";
abc5 = "Age group: 15 - 50";
sexmale = browser.find_element_by_xpath("(//label[@class='radio-inline'][contains(.,'Male')])[2]");
sexfemale = browser.find_element_by_xpath("(//label[@class='radio-inline'][contains(.,'Female')])[2]");
age0to5 = browser.find_element_by_xpath("//input[@value='0 - 5']");
age5to15 = browser.find_element_by_xpath("//input[@value='5 - 15']");
age15to50 = browser.find_element_by_xpath("//input[@value='15 - 50']");
checkbutton2 = browser.find_element_by_xpath("//button[@type='button'][contains(.,'Get values')]");
checkmessage2 = browser.find_element_by_xpath("//p[@class='groupradiobutton']");

sexmale.click();
age0to5.click();
checkbutton2.click();

if (abc1 in checkmessage2.text) and (abc3 in checkmessage2.text):
	print("The output expected: " + "\n" + abc1 + "\n" + abc3);
	print("The output shown: " + checkmessage2.text);

else:
	print("The output expected: " + "\n" + abc1 + "\n" + abc3);
	print("The output shown: " + checkmessage2.text);

sexmale.click();
age5to15.click();
checkbutton2.click();

if (abc1 in checkmessage2.text) and (abc4 in checkmessage2.text):
	print("The output expected: " + "\n" + abc1 + "\n" + abc4);
	print("The output shown: " + checkmessage2.text);

else:
	print("The output expected: " + "\n" + abc1 + "\n" + abc4);
	print("The output shown: " + checkmessage2.text);

sexmale.click();
age15to50.click();
checkbutton2.click();

if (abc1 in checkmessage2.text) and (abc5 in checkmessage2.text):
	print("The output expected: " + "\n" + abc1 + "\n" + abc5);
	print("The output shown: " + checkmessage2.text);

else:
	print("The output expected: " + "\n" + abc1 + "\n" + abc5);
	print("The output shown: " + checkmessage2.text);

sexfemale.click();
age0to5.click();
checkbutton2.click();

if (abc2 in checkmessage2.text) and (abc3 in checkmessage2.text):
	print("The output expected: " + "\n" + abc2 + "\n" + abc3);
	print("The output shown: " + checkmessage2.text);

else:
	print("The output expected: " + "\n" + abc2 + "\n" + abc3);
	print("The output shown: " + checkmessage2.text);

sexfemale.click();
age5to15.click();
checkbutton2.click();

if (abc2 in checkmessage2.text) and (abc4 in checkmessage2.text):
	print("The output expected: " + "\n" + abc2 + "\n" + abc4);
	print("The output shown: " + checkmessage2.text);

else:
	print("The output expected: " + "\n" + abc2 + "\n" + abc4);
	print("The output shown: " + checkmessage2.text);

sexfemale.click();
age15to50.click();
checkbutton2.click();

if (abc2 in checkmessage2.text) and (abc5 in checkmessage2.text):
	print("The output expected: " + "\n" + abc2 + "\n" + abc5);
	print("The output shown: " + checkmessage2.text);

else:
	print("The output expected: " + "\n" + abc2 + "\n" + abc5);
	print("The output shown: " + checkmessage2.text);

#return from Radio Buttons Demo to Main Page
browser.back();
time.sleep(mysecs);

#Open Select Dropdown List screen

InputForms4 = browser.find_element_by_link_text("Input Forms");
InputForms4.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Select Dropdown List").click();

expm1 = mysheet['C1'].value
dropdown1 = browser.find_element_by_id("select-demo");
checkmessage3 = browser.find_element_by_class_name("selected-value");

Select(dropdown1).select_by_value("Wednesday");

a7 = checkmessage3.text

if (expm1 in checkmessage3.text):
	print("The output expected: " + expm1);
	print("The output shown: " + a7);

else:
	print("The output expected: " + expm1);
	print("The output shown: " + a7);

state1 = mysheet['C3'].value
state2 = mysheet['C4'].value
state3 = mysheet['C5'].value
state4 = mysheet['C6'].value
state5 = mysheet['C7'].value
state6 = mysheet['C8'].value
state7 = mysheet['C9'].value
state8 = mysheet['C10'].value
MultiSelect = browser.find_element_by_id("multi-select");
FirstSelectedButton = browser.find_element_by_id("printMe");
GetAllSelectedButton = browser.find_element_by_id("printAll");
checkmsg1 = browser.find_element_by_class_name("getall-selected");

frstoutstate1 = mysheet['C11'].value
frstoutstate2 = mysheet['C12'].value
frstoutstate3 = mysheet['C13'].value
frstoutstate4 = mysheet['C14'].value
frstoutstate5 = mysheet['C15'].value
frstoutstate6 = mysheet['C16'].value
frstoutstate7 = mysheet['C17'].value
frstoutstate8 = mysheet['C18'].value

optoutstate1 = mysheet['C19'].value
optoutstate2 = mysheet['C20'].value
optoutstate3 = mysheet['C21'].value
optoutstate4 = mysheet['C22'].value
optoutstate5 = mysheet['C23'].value
optoutstate6 = mysheet['C24'].value
optoutstate7 = mysheet['C25'].value
optoutstate8 = mysheet['C26'].value

Select(MultiSelect).select_by_value(state1);
FirstSelectedButton.click();

a8 = checkmsg1.text

if (state1 in checkmsg1.text):
	print("The output expected: " + frstoutstate1);
	print("The output shown: " + a8);

else:
	print("The output expected: " + frstoutstate1);
	print("The output shown: " + a8);

GetAllSelectedButton.click();

a9 = checkmsg1.text

if (state1 in checkmsg1.text):
	print("The output expected: " + frstoutstate1);
	print("The output shown: " + a9);

else:
	print("The output expected: " + frstoutstate1);
	print("The output shown: " + a9);

MultiSelect.send_keys(Keys.SHIFT);
Select(MultiSelect).select_by_value(state2);
FirstSelectedButton.click();

if (state2 in checkmsg1.text):
	print("The output expected: " + frstoutstate1 + optoutstate2);
	print("The output shown: " + checkmsg1.text);

else:
	print("The output expected: " + frstoutstate1 + optoutstate2);
	print("The output shown: " + checkmsg1.text);

GetAllSelectedButton.click();

if (state2 in checkmsg1.text):
	print("The output expected: " + frstoutstate1 + "\n" + optoutstate2);
	print("The output shown: " + checkmsg1.text);

else:
	print("The output expected: " + frstoutstate1 + "\n" + optoutstate2);
	print("The output shown: " + checkmsg1.Text);

#return from Select Dropdown List to Main Page
browser.back();
time.sleep(mysecs);

#Open Input Form Submit screen

InputForms5 = browser.find_element_by_link_text("Input Forms");
InputForms5.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Input Form Submit").click();

firstname = mysheet['D1'].value
lastname = mysheet['D2'].value
email = mysheet['D3'].value
phone = mysheet['D4'].value
address = mysheet['D5'].value
city = mysheet['D6'].value
zipcode = mysheet['D7'].value
websiteurl = mysheet['D8'].value
mycomment = mysheet['D9'].value

browser.find_element_by_name("first_name").send_keys(firstname);
browser.find_element_by_name("last_name").send_keys(lastname);
browser.find_element_by_name("email").send_keys(email);
browser.find_element_by_name("phone").send_keys(phone);
browser.find_element_by_name("address").send_keys(address);
browser.find_element_by_name("city").send_keys(city);
mystate1 = browser.find_element_by_css_selector("select.form-control");
Select(mystate1).select_by_visible_text("Pennsylvania");
browser.find_element_by_name("zip").send_keys(zipcode);
browser.find_element_by_name("website").send_keys(websiteurl);

radio11 = browser.find_element_by_xpath("//input[contains(@value,'yes')]");
radio21 = browser.find_element_by_xpath("//input[contains(@value,'no')]");
radio11.click();
radio21.click();

browser.find_element_by_name("comment").send_keys(mycomment);
mybtn11 = browser.find_element_by_xpath("//button[contains(@type,'submit')]");
mybtn11.click();

#Open Ajax Form Submit screen

InputForms6 = browser.find_element_by_link_text("Input Forms");
InputForms6.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Ajax Form Submit").click();

myname = mysheet['E1'].value
mytextarea = mysheet['E2'].value
browser.find_element_by_id("title").send_keys(myname);
browser.find_element_by_id("description").send_keys(mytextarea);
mysubmitbtn = browser.find_element_by_id("btn-submit");
mysubmitbtn.click();

expsubmittext = mysheet['E3'].value
mysubmittext = browser.find_element_by_id("submit-control");

time.sleep(mysecs);

a10 = mysubmittext.text

if (expsubmittext in mysubmittext.text):
	print("The output expected: " + expsubmittext);
	print("The output shown: " + a10);

else:
	print("The output expected: " + expsubmittext);
	print("The output shown: " + a10);

#Open Ajax Form Submit screen

InputForms7 = browser.find_element_by_link_text("Input Forms");
InputForms7.send_keys(Keys.DOWN);
browser.find_element_by_link_text("JQuery Select dropdown").click();

mysearch = "n";
SelectCountry = browser.find_element_by_xpath("(//span[contains(@class,'select2-selection__arrow')])[1]");
SelectCountry.click();
searchCountry = browser.find_element_by_xpath("(//input[contains(@class,'select2-search__field')])[2]");
searchCountry.send_keys(mysearch);
searchCountry.send_keys(Keys.ENTER);
SelectCountry.click();
browser.find_element_by_xpath("//li[contains(.,'Netherlands')]").click();

SelectState = browser.find_element_by_xpath("//input[@class='select2-search__field']");
SelectState.click();
browser.find_element_by_xpath("//li[contains(.,'Pennsylvania')]").click();

SelectUSOutlyingTerritories = browser.find_element_by_xpath("(//span[contains(@class,'select2-selection__arrow')])[2]");
SelectUSOutlyingTerritories.click();

mysearchterritories = "g";
searchUSOutlyingTerritories = browser.find_element_by_xpath("(//input[contains(@class,'select2-search__field')])[2]");
searchUSOutlyingTerritories.send_keys(mysearchterritories);
searchUSOutlyingTerritories.send_keys(Keys.ENTER);
SelectUSOutlyingTerritories.click();
browser.find_element_by_xpath("//li[contains(.,'Virgin Islands')]").click();

Selectfile = browser.find_element_by_id("files");
Selectfile.click();
Selectfile.send_keys(Keys.DOWN);
Selectfile.send_keys(Keys.ENTER);
Selectfile.send_keys(Keys.DOWN);
Selectfile.send_keys(Keys.DOWN);
Selectfile.send_keys(Keys.DOWN);
Selectfile.send_keys(Keys.DOWN);
Selectfile.send_keys(Keys.DOWN);
Selectfile.send_keys(Keys.DOWN);
Selectfile.send_keys(Keys.ENTER);

#Open Bootstrap Date Picker screen

InputForms8 = browser.find_element_by_link_text("Date pickers");
InputForms8.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Bootstrap Date Picker").click();

browser.find_element_by_xpath("//i[contains(@class,'glyphicon glyphicon-th')]").click();
browser.find_element_by_xpath("(//td[contains(.,'14')])[1]").click();
browser.find_element_by_xpath("//i[contains(@class,'glyphicon glyphicon-th')]").click();
browser.find_element_by_xpath("(//th[contains(.,'Today')])[1]").click();
browser.find_element_by_xpath("//i[contains(@class,'glyphicon glyphicon-th')]").click();
browser.find_element_by_xpath("(//th[contains(.,'Clear')])[1]").click();
browser.find_element_by_xpath("//i[contains(@class,'glyphicon glyphicon-th')]").click();
browser.find_element_by_xpath("(//td[contains(.,'30')])[1]").click();
browser.find_element_by_xpath("//input[contains(@placeholder,'Start date')]").click();
browser.find_element_by_xpath("(//td[contains(.,'4')])[2]").click();
browser.find_element_by_xpath("//input[contains(@placeholder,'End date')]").click();
browser.find_element_by_xpath("(//td[contains(.,'20')])[1]").click();

#Open JQuery Date Picker screen

InputForms9 = browser.find_element_by_link_text("Date pickers");
InputForms9.send_keys(Keys.DOWN);
browser.find_element_by_link_text("JQuery Date Picker").click();
browser.find_element_by_xpath("//input[contains(@name,'from')]").click();
browser.find_element_by_xpath("(//a[contains(.,'3')])[2]").click();
browser.find_element_by_xpath("//input[contains(@name,'to')]").click();
browser.find_element_by_xpath("//a[contains(.,'24')]").click();

#Open Table Pagination screen

InputForms10 = browser.find_element_by_link_text("Table");
InputForms10.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Table Pagination").click();
browser.find_element_by_xpath("//a[contains(.,'2')]").click();
browser.find_element_by_xpath("//a[contains(.,'3')]").click();
browser.find_element_by_xpath("//a[contains(.,'2')]").click();
browser.find_element_by_xpath("//a[contains(.,'1')]").click();
browser.find_element_by_xpath("//a[contains(@class,'next_link')]").click();
browser.find_element_by_xpath("//a[contains(@class,'next_link')]").click();
browser.find_element_by_xpath("//a[contains(@class,'prev_link')]").click();
browser.find_element_by_xpath("//a[contains(@class,'prev_link')]").click();

#Open Table Data Search screen

InputForms11 = browser.find_element_by_link_text("Table");
InputForms11.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Table Data Search").click();

mytest1 = mysheet['F1'].value
mytest2 = mysheet['F2'].value
mytest3 = mysheet['F3'].value

InputBox1 = browser.find_element_by_xpath("//input[contains(@data-action,'filter')]");
InputBox1.click();
InputBox1.send_keys(mytest1);
InputBox1.send_keys(Keys.ENTER);

OutBox1 = browser.find_element_by_xpath("//td[contains(.,'Wireframes')]");

a11 = OutBox1.text

if (mytest1 in OutBox1.text):
	print("The output expected: " + mytest1);
	print("The output shown: " + a11);

else:
	print("The output expected: " + mytest1);
	print("The output shown: " + a11);

InputBox1.clear();

InputBox1.send_keys(mytest2);
InputBox1.send_keys(Keys.ENTER);

OutBox2 = browser.find_element_by_xpath("//td[contains(.,'Jane Doe')]");

a12 = OutBox2.text

if (mytest2 in OutBox2.text):
	print("The output expected: " + mytest2);
	print("The output shown: " + a12);

else:
	print("The output expected: " + mytest2);
	print("The output shown: " + a12);

InputBox1.clear();

InputBox1.send_keys(mytest3);
InputBox1.send_keys(Keys.ENTER);

OutBox3 = browser.find_element_by_xpath("//td[contains(.,'completed')]");

a13 = OutBox3.text

if (mytest3 in OutBox3.text):
	print("The output expected: " + mytest3);
	print("The output shown: " + a13);

else:
	print("The output expected: " + mytest3);
	print("The output shown: " + a13);

InputBox1.clear();
InputBox1.send_keys(Keys.ENTER);

browser.find_element_by_xpath("//button[contains(.,'Filter')]").click();

mytest4 = mysheet['F4'].value
mytest5 = mysheet['F5'].value
mytest6 = mysheet['F6'].value
mytest7 = mysheet['F7'].value

InputBox11 = browser.find_element_by_xpath("//input[contains(@placeholder,'#')]");

InputBox11.click();
InputBox11.send_keys(mytest4);
InputBox11.send_keys(Keys.ENTER);

OutBox11 = browser.find_element_by_xpath("(//td[contains(.,'3')])[3]");

a14 = OutBox11.text

if (str(mytest4) in OutBox11.text):
	print("The output expected: " + str(mytest4));
	print("The output shown: " + a14);

else:
	print("The output expected: " + str(mytest4));
	print("The output shown: " + a14);

InputBox11.clear();

InputBox12 = browser.find_element_by_xpath("//input[contains(@placeholder,'Username')]");

InputBox12.click();
InputBox12.send_keys(mytest5);
InputBox12.send_keys(Keys.ENTER);

OutBox12 = browser.find_element_by_xpath("//td[contains(.,'jacobs')]");

a15 = OutBox12.text

if (mytest5 in OutBox12.text):
	print("The output expected: " + mytest5);
	print("The output shown: " + a15);

else:
	print("The output expected: " + mytest5);
	print("The output shown: " + a15);

InputBox12.clear();

InputBox13 = browser.find_element_by_xpath("//input[contains(@placeholder,'First Name')]");

InputBox13.click();
InputBox13.send_keys(mytest6);
InputBox13.send_keys(Keys.ENTER);

OutBox13 = browser.find_element_by_xpath("//td[contains(.,'Byron')]");

a16 = OutBox13.text

if (mytest6 in OutBox13.text):
	print("The output expected: " + mytest6);
	print("The output shown: " + a16);

else:
	print("The output expected: " + mytest6);
	print("The output shown: " + a16);

InputBox13.clear();

InputBox14 = browser.find_element_by_xpath("//input[contains(@placeholder,'Last Name')]");

InputBox14.click();
InputBox14.send_keys(mytest7);
InputBox13.send_keys(Keys.ENTER);

OutBox14 = browser.find_element_by_xpath("//td[contains(.,'Samuels')]");

a17 = OutBox14.text

if (mytest7 in OutBox14.text):
	print("The output expected: " + mytest7);
	print("The output shown: " + a17);

else:
	print("The output expected: " + mytest7);
	print("The output shown: " + a17);

InputBox14.clear();

#Open Table Filter screen

InputForms12 = browser.find_element_by_link_text("Table");
InputForms12.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Table Filter").click();

greenbtn = browser.find_element_by_xpath("//button[contains(.,'Green')]");
orangebtn = browser.find_element_by_xpath("//button[contains(.,'Orange')]");
redbtn = browser.find_element_by_xpath("//button[contains(.,'Red')]");
allbtn = browser.find_element_by_xpath("//button[contains(.,'All')]");
check1 = browser.find_element_by_css_selector(".table > tbody:nth-child(1) > tr:nth-child(1) > td:nth-child(3) > div:nth-child(1) > a:nth-child(1) > i:nth-child(1)");
check2 = browser.find_element_by_css_selector(".table > tbody:nth-child(1) > tr:nth-child(2) > td:nth-child(3) > div:nth-child(1) > a:nth-child(1) > i:nth-child(1)");
check3 = browser.find_element_by_css_selector(".table > tbody:nth-child(1) > tr:nth-child(3) > td:nth-child(3) > div:nth-child(1) > a:nth-child(1) > i:nth-child(1)");
check4 = browser.find_element_by_css_selector(".table > tbody:nth-child(1) > tr:nth-child(4) > td:nth-child(3) > div:nth-child(1) > a:nth-child(1) > i:nth-child(1)");
check5 = browser.find_element_by_css_selector(".table > tbody:nth-child(1) > tr:nth-child(5) > td:nth-child(3) > div:nth-child(1) > a:nth-child(1) > i:nth-child(1)");

time.sleep(mysecs);
greenbtn.click();

print("Click Green Button: ");
print("check1 green should be shown: " + str(check1.is_displayed()));
print("check2 orange should be hidden: " + str(check2.is_displayed()));
print("check3 red should be hidden: " + str(check3.is_displayed()));
print("check4 green should be shown: " + str(check4.is_displayed()));
print("check5 orange should be hidden: " + str(check5.is_displayed()));

time.sleep(mysecs);
orangebtn.click();

print("Click Orange Button: ");
print("check1 green should be hidden: " + str(check1.is_displayed()));
print("check2 orange should be shown: " + str(check2.is_displayed()));
print("check3 red should be hidden: " + str(check3.is_displayed()));
print("check4 green should be hidden: " + str(check4.is_displayed()));
print("check5 orange should be shown: " + str(check5.is_displayed()));

time.sleep(mysecs);
redbtn.click();

print("Click Red Button: ");
print("check1 green should be hidden: " + str(check1.is_displayed()));
print("check2 orange should be hidden: " + str(check2.is_displayed()));
print("check3 red should be shown: " + str(check3.is_displayed()));
print("check4 green should be hidden: " + str(check4.is_displayed()));
print("check5 orange should be hidden: " + str(check5.is_displayed()));

time.sleep(mysecs);
allbtn.click();

print("Click All Button: ");
print("check1 green should be shown: " + str(check1.is_displayed()));
print("check2 orange should be shown: " + str(check2.is_displayed()));
print("check3 red should be shown: " + str(check3.is_displayed()));
print("check4 green should be shown: " + str(check4.is_displayed()));
print("check5 orange should be shown: " + str(check5.is_displayed()));

time.sleep(mysecs);

#Open Table Sort & Search screen

InputForms13 = browser.find_element_by_link_text("Table");
InputForms13.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Table Sort & Search").click();

mymessage1 = mysheet['G1'].value
mymessage2 = mysheet['G2'].value
mymessage3 = mysheet['G3'].value

browser.find_element_by_xpath("//select[contains(@name,'length')]").send_keys("50");
browser.find_element_by_xpath("//select[contains(@name,'length')]").click();
time.sleep(mysecs);
mymessagebox = browser.find_element_by_xpath("//div[@class='dataTables_info']");

a18 = mymessagebox.text

if (mymessage1 in mymessagebox.text):
	print("The output expected: " + mymessage1);
	print("The output shown: " + a18);

else:
	print("The output expected: " + mymessage1);
	print("The output shown: " + a18);

time.sleep(mysecs);
browser.find_element_by_xpath("//select[contains(@name,'length')]").send_keys("25");
browser.find_element_by_xpath("//select[contains(@name,'length')]").click();

a19 = mymessagebox.text

if (mymessage2 in mymessagebox.text):
	print("The output expected: " + mymessage2);
	print("The output shown: " + a19);

else:
	print("The output expected: " + mymessage2);
	print("The output shown: " + a19);

time.sleep(mysecs);
browser.find_element_by_xpath("//select[contains(@name,'length')]").click();
browser.find_element_by_xpath("//select[contains(@name,'length')]").send_keys(Keys.ARROW_UP);
browser.find_element_by_xpath("//select[contains(@name,'length')]").send_keys(Keys.ENTER);

a20 = mymessagebox.text

if (mymessage3 in mymessagebox.text):
	print("The output expected: " + mymessage3);
	print("The output shown: " + a20);

else:
	print("The output expected: " + mymessage3);
	print("The output shown: " + a20);

#next
browser.find_element_by_xpath("//a[contains(.,'Next')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//a[@class='paginate_button '][contains(.,'3')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//select[contains(@name,'length')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//a[contains(.,'Next')]").click();
time.sleep(mysecs);

#prior
browser.find_element_by_xpath("//a[contains(.,'Previous')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//a[@class='paginate_button '][contains(.,'2')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//a[contains(.,'Previous')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//a[contains(.,'Previous')]").click();
time.sleep(mysecs);

browser.find_element_by_xpath("//select[contains(@name,'length')]").send_keys("100");
browser.find_element_by_xpath("//select[contains(@name,'length')]").send_keys(Keys.ENTER);

myname111 = mysheet['G5'].value
myposition = mysheet['G6'].value
myoffice = mysheet['G7'].value
myage = mysheet['G8'].value
mystartdate = mysheet['G9'].value
mysalary = mysheet['G10'].value

time.sleep(mysecs);

browser.find_element_by_xpath("//input[@type='search']").send_keys(myname111);
browser.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER);
browser.find_element_by_xpath("//input[@type='search']").clear();
time.sleep(mysecs);

browser.find_element_by_xpath("//input[@type='search']").send_keys(myposition);
browser.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER);
browser.find_element_by_xpath("//input[@type='search']").clear();
time.sleep(mysecs);

browser.find_element_by_xpath("//input[@type='search']").send_keys(myoffice);
browser.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER);
browser.find_element_by_xpath("//input[@type='search']").clear();
time.sleep(mysecs);

browser.find_element_by_xpath("//input[@type='search']").send_keys(str(myage));
browser.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER);
browser.find_element_by_xpath("//input[@type='search']").clear();
time.sleep(mysecs);

browser.find_element_by_xpath("//input[@type='search']").send_keys(mystartdate);
browser.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER);
browser.find_element_by_xpath("//input[@type='search']").clear();
time.sleep(mysecs);

browser.find_element_by_xpath("//input[@type='search']").send_keys(str(mysalary));
browser.find_element_by_xpath("//input[@type='search']").send_keys(Keys.ENTER);
browser.find_element_by_xpath("//input[@type='search']").clear();

time.sleep(mysecs);

browser.find_element_by_xpath("//input[@type='search']").send_keys(Keys.CLEAR);

#Click on column headings to sort
browser.find_element_by_xpath("//th[contains(.,'Name')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//th[contains(.,'Position')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//th[contains(.,'Office')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//th[contains(.,'Age')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//th[contains(.,'Start date')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//th[contains(.,'Salary')]").click();

#Open Table Data Download screen
InputForms14 = browser.find_element_by_link_text("Table");
InputForms14.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Table Data Download").click();

#Open JQuery Download Progress bars screen
InputForms15 = browser.find_element_by_link_text("Progress Bars");
InputForms15.send_keys(Keys.DOWN);
browser.find_element_by_link_text("JQuery Download Progress bars").click();

#browser.implicitly_wait(mysecs);
time.sleep(mysecs);
browser.find_element_by_xpath("//button[contains(.,'Start Download')]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("(//button[contains(@type,'button')])[3]").click();

#Open Bootstrap Progress bar screen

InputForms16 = browser.find_element_by_link_text("Progress Bars");
InputForms16.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Bootstrap Progress bar").click();

time.sleep(mysecs);
browser.find_element_by_xpath("(//button[@type='button'])[2]").click();

time.sleep(mysecs * 2);

OneHundredPercnt = browser.find_element_by_xpath("//div[@class='percenttext']");

if ("100%" in OneHundredPercnt.text):
	print("The output expected: " + "100%");
	print("The output shown: " + OneHundredPercnt.text);

else:
	print("The output expected: " + "100%");
	print("The output shown: " + OneHundredPercnt.text);

#Open Drag & Drop Sliders screen

InputForms17 = browser.find_element_by_link_text("Progress Bars");
InputForms17.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Drag & Drop Sliders").click();
time.sleep(mysecs);

#grey
greybar = browser.find_element_by_xpath("//input[@onchange='range.value=value']");
numbergreybar1 = 50;
numbergreybar2 = -30;
greyslider = ActionChains(browser);
greyslider.click_and_hold(greybar).move_by_offset(numbergreybar1, 0).release().perform();
time.sleep(mysecs);
greyslider.click_and_hold(greybar).move_by_offset(numbergreybar2, 0).release().perform();
time.sleep(mysecs);

#green
greenbar = browser.find_element_by_xpath("//input[@onchange='rangeSuccess.value=value']");
numbergreenbar1 = 60;
numbergreenbar2 = -40;
greenslider = ActionChains(browser);
greenslider.click_and_hold(greenbar).move_by_offset(numbergreenbar1, 0).release().perform();
time.sleep(mysecs);
greenslider.click_and_hold(greenbar).move_by_offset(numbergreenbar2, 0).release().perform();
time.sleep(mysecs);

#orange
orangebar = browser.find_element_by_xpath("//input[@onchange='rangeWarning.value=value']");
numberorangebar1 = 80;
numberorangebar2 = -50;
orangeslider = ActionChains(browser);
orangeslider.click_and_hold(orangebar).move_by_offset(numberorangebar1, 0).release().perform();
time.sleep(mysecs);
orangeslider.click_and_hold(orangebar).move_by_offset(numberorangebar2, 0).release().perform();
time.sleep(mysecs);

#dark blue
darkbluebar = browser.find_element_by_xpath("//input[@onchange='rangePrimary.value=value']");
numberdarkbluebar1 = 70;
numberdarkbluebar2 = -80;
darkblueslider = ActionChains(browser);
darkblueslider.click_and_hold(darkbluebar).move_by_offset(numberdarkbluebar1, 0).release().perform();
browser.implicitly_wait(mysecs);
time.sleep(mysecs);
darkblueslider.click_and_hold(darkbluebar).move_by_offset(numberdarkbluebar2, 0).release().perform();
time.sleep(mysecs);

#light blue
lightbluebar = browser.find_element_by_xpath("//input[@onchange='rangeInfo.value=value']");
numberlightbluebar1 = 80;
numberlightbluebar2 = -80;
lightblueslider = ActionChains(browser);
lightblueslider.click_and_hold(lightbluebar).move_by_offset(numberlightbluebar1, 0).release().perform();
time.sleep(mysecs);
lightblueslider.click_and_hold(lightbluebar).move_by_offset(numberlightbluebar2, 0).release().perform();
time.sleep(mysecs);

#red
redbar = browser.find_element_by_xpath("//input[@onchange='rangeDanger.value=value']");
numberredbar1 = 50;
numberredbar2 = -90;
redslider = ActionChains(browser);
redslider.click_and_hold(redbar).move_by_offset(numberredbar1, 0).release().perform();
time.sleep(mysecs);
redslider.click_and_hold(redbar).move_by_offset(numberredbar2, 0).release().perform();
time.sleep(mysecs);

#Open Bootstrap Alerts screen

InputForms18 = browser.find_element_by_link_text("Alerts & Modals");
InputForms18.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Bootstrap Alerts").click();

m1 = mysheet['H1'].value
m2 = mysheet['H2'].value
m3 = mysheet['H3'].value
m4 = mysheet['H4'].value
m5 = mysheet['H5'].value
m6 = mysheet['H6'].value
m7 = mysheet['H7'].value
m8 = mysheet['H8'].value

browser.find_element_by_xpath("//button[@id='autoclosable-btn-success']").click();
alert1 = browser.find_element_by_xpath("//div[contains(@class,'alert alert-success alert-autocloseable-success')]");

a21 = alert1.text

if (m1 in alert1.text):
	print("The output expected: " + m1);
	print("The output shown: " + a21);

else:
	print("The output expected: " + m1);
	print("The output shown: " + a21);

time.sleep(mysecs);

browser.find_element_by_xpath("//button[@id='normal-btn-success']").click();
alert2 = browser.find_element_by_xpath("//div[contains(@class,'alert alert-success alert-normal-success')]");

a22 = alert2.text

if (m2 in alert2.text):
	print("The output expected: " + m2);
	print("The output shown: " + a22);

else:
	print("The output expected: " + m2);
	print("The output shown: " + a22);

time.sleep(mysecs);

browser.find_element_by_xpath("(//button[@type='button'][contains(.,'×')])[1]").click();

browser.find_element_by_xpath("//button[@id='normal-btn-success']").click();
alert3 = browser.find_element_by_xpath("//div[contains(@class,'alert alert-warning alert-autocloseable-warning')]");

a23 = alert3.text

if (m3 in alert3.text):
	print("The output expected: " + m3);
	print("The output shown: " + a23);

else:
	print("The output expected: " + m3);
	print("The output shown: " + a23);

time.sleep(mysecs);

browser.find_element_by_xpath("//button[contains(.,'Normal warning message')]").click();
alert4 = browser.find_element_by_xpath("//div[contains(@class,'alert alert-warning alert-normal-warning')]");

a24 = alert4.text

if (m4 in alert4.text):
	print("The output expected: " + m4);
	print("The output shown: " + a24);

else:
	print("The output expected: " + m4);
	print("The output shown: " + a24);

time.sleep(mysecs);

browser.find_element_by_xpath("(//button[@type='button'][contains(.,'×')])[2]").click();

time.sleep(mysecs);

browser.find_element_by_xpath("//button[contains(.,'Autocloseable danger message')]").click();
alert5 = browser.find_element_by_xpath("//div[contains(@class,'alert alert-danger alert-autocloseable-danger')]");

a25 = alert5.text

if (m5 in alert5.text):
	print("The output expected: " + m5);
	print("The output shown: " + a25);

else:
	print("The output expected: " + m5);
	print("The output shown: " + a25);

time.sleep(mysecs);

browser.find_element_by_xpath("//button[contains(.,'Normal danger message')]").click();
alert6 = browser.find_element_by_xpath("//div[contains(@class,'alert alert-danger alert-normal-danger')]");

a26 = alert6.text

if (m6 in alert6.text):
	print("The output expected: " + m6);
	print("The output shown: " + a26);

else:
	print("The output expected: " + m6);
	print("The output shown: " + a26);

time.sleep(mysecs);
browser.find_element_by_xpath("(//button[@type='button'][contains(.,'×')])[3]").click();

browser.find_element_by_xpath("//button[contains(.,'Autocloseable info message')]").click();
alert7 = browser.find_element_by_xpath("//div[contains(@class,'alert alert-info alert-autocloseable-info')]");

a27 = alert7.text

if (m7 in alert7.text):
	print("The output expected: " + m7);
	print("The output shown: " + a27);

else:
	print("The output expected: " + m7);
	print("The output shown: " + a27);

time.sleep(mysecs);

browser.find_element_by_xpath("//button[contains(.,'Normal info message')]").click();
alert8 = browser.find_element_by_xpath("//div[contains(@class,'alert alert-info alert-normal-info')]");

a28 = alert8.text

if (m8 in alert8.text):
	print("The output expected: " + m8);
	print("The output shown: " + a28);

else:
	print("The output expected: " + m8);
	print("The output shown: " + a28);

time.sleep(mysecs);

browser.find_element_by_xpath("(//button[@type='button'][contains(.,'×')])[4]").click();

browser.find_element_by_xpath("(//button[@type='button'][contains(.,'×')])[1]").click();

#Open Bootstrap Modals screen

InputForms19 = browser.find_element_by_link_text("Alerts & Modals");
InputForms19.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Bootstrap Modals").click();

browser.find_element_by_xpath("//a[@href='#myModal0']").click();
time.sleep(mysecs);
browser.find_element_by_xpath("(//a[@href='#'][contains(.,'Close')])[1]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//a[@href='#myModal0']").click();
time.sleep(mysecs);
browser.find_element_by_xpath("(//a[@href='#'][contains(.,'Save changes')])[1]").click();
time.sleep(mysecs);

browser.find_element_by_xpath("//a[@href='#myModal']").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//a[@href='#myModal2']").click();
time.sleep(mysecs);
browser.find_element_by_xpath("(//a[@href='#'][contains(.,'Close')])[3]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//a[@href='#myModal2']").click();
time.sleep(mysecs);
browser.find_element_by_xpath("(//a[@href='#'][contains(.,'Save changes')])[3]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//a[@href='#myModal']").click();
time.sleep(mysecs);
browser.find_element_by_xpath("(//a[@href='#'][contains(.,'Close')])[2]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("//a[@href='#myModal']").click();
time.sleep(mysecs);
browser.find_element_by_xpath("(//a[@href='#'][contains(.,'Save changes')])[2]").click();

#Open Window Popup Modal screen

InputForms20 = browser.find_element_by_link_text("Alerts & Modals");
InputForms20.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Window Popup Modal").click();

current = browser.current_window_handle;
newHandle11 = browser.find_element_by_xpath("//a[contains(.,'Follow On Twitter')]").click();
time.sleep(mysecs);
newHandle10 = list(browser.window_handles);

for handle1 in newHandle10:
	time.sleep(mysecs);
	browser.switch_to.window(handle1);
	if (browser.title!= "Selenium Easy - Window Popup Modal Demo"):
		browser.close();

browser.switch_to.window(current);

time.sleep(mysecs);
newHandle12 = browser.find_element_by_xpath("//a[contains(.,'Like us On Facebook')]").click();
time.sleep(mysecs);
newHandle20 = list(browser.window_handles);

for handle2 in newHandle20:
	time.sleep(mysecs);
	browser.switch_to.window(handle2);
	if (browser.title!= "Selenium Easy - Window Popup Modal Demo"):
		browser.close();

time.sleep(mysecs);
browser.switch_to.window(current);

newHandle3 = browser.find_element_by_xpath("//a[contains(.,'Follow Twitter & Facebook')]").click();

newHandle30 = list(browser.window_handles);

for handle3 in newHandle30:
	time.sleep(mysecs);
	browser.switch_to.window(handle3);
	if (browser.title!= "Selenium Easy - Window Popup Modal Demo"):
		browser.close();

time.sleep(mysecs);
browser.switch_to.window(current);

newHandle4 = browser.find_element_by_xpath("//a[contains(.,'Follow All')]").click();

newHandle31 = list(browser.window_handles);

for handle4 in newHandle31:
	time.sleep(mysecs);
	browser.switch_to.window(handle4);
	if (browser.title!= "Selenium Easy - Window Popup Modal Demo"):
		browser.close();

browser.switch_to.window(current);

time.sleep(mysecs);

#Open Progress Bar Modal screen

InputForms21 = browser.find_element_by_link_text("Alerts & Modals");
InputForms21.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Progress Bar Modal").click();

browser.find_element_by_xpath("(//button[@type='button'])[2]").click();
time.sleep(mysecs);
browser.find_element_by_xpath("(//button[@type='button'])[3]").click();
time.sleep(mysecs * 2);
browser.find_element_by_xpath("(//button[@type='button'])[4]").click();
time.sleep(mysecs * 2);

#Open Javascript Alerts screen

InputForms22 = browser.find_element_by_link_text("Alerts & Modals");
InputForms22.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Javascript Alerts").send_keys(Keys.ENTER);

time.sleep(mysecs);

browser.find_element_by_xpath("//button[@class='btn btn-default']").click();

alert11 = browser.switch_to.alert;
a11 = alert11.text;
browser.implicitly_wait(mysecs);
alert11.accept();

print("The output: " + a11);

time.sleep(mysecs);
browser.find_element_by_xpath("(//button[contains(@class,'btn btn-default btn-lg')])[1]").click();

alert12 = browser.switch_to.alert;
time.sleep(mysecs);
alert12.dismiss();

m11 = "You pressed Cancel!";

alert2cancel = browser.find_element_by_xpath("//p[contains(.,'You pressed Cancel!')]");

a29 = alert2cancel.text

if (m11 in alert2cancel.text):
	print("The output expected: " + m11);
	print("The output shown: " + a29);

else:
	print("The output expected: " + m11);
	print("The output shown: " + a29);

time.sleep(mysecs);
browser.find_element_by_xpath("(//button[contains(@class,'btn btn-default btn-lg')])[1]").click();

alert13 = browser.switch_to.alert;
time.sleep(mysecs);
alert13.accept();

m12 = "You pressed OK!";

alert2accept = browser.find_element_by_xpath("//p[contains(.,'You pressed OK!')]");

a30 = alert2accept.text

if (m12 in alert2accept.text):
	print("The output expected: " + m12);
	print("The output shown: " + a30);

else:
	print("The output expected: " + m12);
	print("The output shown: " + a30);

time.sleep(mysecs);
browser.find_element_by_xpath("//button[@class='btn btn-default btn-lg'][contains(.,'Click for Prompt Box')]").click();

alert14 = browser.switch_to.alert;
time.sleep(mysecs);
alert14.dismiss();

time.sleep(mysecs);
m14 = "test";

browser.find_element_by_xpath("//button[@class='btn btn-default btn-lg'][contains(.,'Click for Prompt Box')]").click();

alert15 = browser.switch_to.alert;
time.sleep(mysecs);
alert15.send_keys(m14);
time.sleep(mysecs);
alert15.accept();

popuptext = browser.find_element_by_id("prompt-demo");

m15 = "You have entered" + "'" + m14 + "'!";

a31 = popuptext.text

if (m15 in popuptext.text):
	print("The output expected: " + m15);
	print("The output shown: " + a31);

else:
	print("The output expected: " + m15);
	print("The output shown: " + a31);

time.sleep(mysecs);

#Open Javascript Alerts screen

InputForms23 = browser.find_element_by_link_text("Alerts & Modals");
InputForms23.send_keys(Keys.DOWN);
browser.find_element_by_link_text("File Download").send_keys(Keys.ENTER);

myinputtext = "Transportation moves people and goods from one place to another using a variety of vehicles.";

inputtext = browser.find_element_by_id("textbox");
time.sleep(mysecs);
inputtext.send_keys(myinputtext);
time.sleep(mysecs);
generatefile = browser.find_element_by_id("create");
time.sleep(mysecs);
generatefile.click();
time.sleep(mysecs);
downloadfile = browser.find_element_by_xpath("(//a[contains(.,'Download')])[7]");
downloadfile.click();
time.sleep(mysecs);

#Open Bootstrap List Box screen

InputForms24 = browser.find_element_by_link_text("List Box");
InputForms24.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Bootstrap List Box").send_keys(Keys.ENTER);

r1 = "a";
r2 = "b";

search1 = browser.find_element_by_xpath("(//input[contains(@type,'text')])[1]");
search2 = browser.find_element_by_xpath("(//input[contains(@type,'text')])[2]");

elementleft1 = browser.find_element_by_xpath("//li[@class='list-group-item'][contains(.,'bootstrap-duallist')]");
elementleft2 = browser.find_element_by_xpath("(//li[@class='list-group-item'][contains(.,'Dapibus ac facilisis in')])[1]");
elementleft3 = browser.find_element_by_xpath("(//li[@class='list-group-item'][contains(.,'Morbi leo risus')])[1]");
elementleft4 = browser.find_element_by_xpath("(//li[@class='list-group-item'][contains(.,'Porta ac consectetur ac')])[1]");
elementleft5 = browser.find_element_by_xpath("(//li[@class='list-group-item'][contains(.,'Vestibulum at eros')])[1]");
elementleftselectall = browser.find_element_by_xpath("(//i[contains(@class,'glyphicon glyphicon-unchecked')])[1]");
elementmovetoleft = browser.find_element_by_xpath("//button[contains(@class,'btn btn-default btn-sm move-left')]");

elementright1 = browser.find_element_by_xpath("//li[@class='list-group-item'][contains(.,'Cras justo odio')]");
elementright2 = browser.find_element_by_xpath("(//li[@class='list-group-item'][contains(.,'Dapibus ac facilisis in')])[2]");
elementright3 = browser.find_element_by_xpath("(//li[@class='list-group-item'][contains(.,'Morbi leo risus')])[2]");
elementright4 = browser.find_element_by_xpath("(//li[@class='list-group-item'][contains(.,'Porta ac consectetur ac')])[2]");
elementright5 = browser.find_element_by_xpath("(//li[@class='list-group-item'][contains(.,'Vestibulum at eros')])[2]");
elementrightselectall = browser.find_element_by_xpath("(//i[contains(@class,'glyphicon glyphicon-unchecked')])[2]");
elementmovetoright = browser.find_element_by_xpath("//span[contains(@class,'glyphicon glyphicon-chevron-right')]");

search1.send_keys(r1);
time.sleep(mysecs);
search2.send_keys(r2);
time.sleep(mysecs);
search1.clear();
search1.send_keys(Keys.ENTER);
time.sleep(mysecs);
search2.clear();
search2.send_keys(Keys.ENTER);
time.sleep(mysecs);
elementleft1.click();
time.sleep(mysecs);
elementleft2.click();
time.sleep(mysecs);
elementleft3.click();
time.sleep(mysecs);
elementleft4.click();
time.sleep(mysecs);
elementleft5.click();
time.sleep(mysecs);
elementright1.click();
time.sleep(mysecs);
elementright2.click();
time.sleep(mysecs);
elementright3.click();
time.sleep(mysecs);
elementright4.click();
time.sleep(mysecs);
elementright5.click();
time.sleep(mysecs);
elementleft1.click();
time.sleep(mysecs);
elementleft2.click();
time.sleep(mysecs);
elementleft3.click();
time.sleep(mysecs);
elementleft4.click();
time.sleep(mysecs);
elementleft5.click();
time.sleep(mysecs);
elementright1.click();
time.sleep(mysecs);
elementright2.click();
time.sleep(mysecs);
elementright3.click();
time.sleep(mysecs);
elementright4.click();
time.sleep(mysecs);
elementright5.click();
time.sleep(mysecs);
elementleft1.click();
time.sleep(mysecs);
elementleft2.click();
time.sleep(mysecs);
elementmovetoright.click();
time.sleep(mysecs);
elementright2.click();
time.sleep(mysecs);
elementright3.click();
time.sleep(mysecs);
elementmovetoleft.click();
time.sleep(mysecs);
elementleftselectall.click();
time.sleep(mysecs);
elementmovetoright.click();
time.sleep(mysecs);
elementrightselectall.click();
elementmovetoleft.click();
time.sleep(mysecs);

#Open JQuery List Box screen

InputForms25 = browser.find_element_by_link_text("List Box");
InputForms25.send_keys(Keys.DOWN);
browser.find_element_by_link_text("JQuery List Box").send_keys(Keys.ENTER);

myname1 = browser.find_element_by_xpath("//option[@data-id='1'][contains(.,'Isis')]");
myname2 = browser.find_element_by_xpath("//option[@data-id='2'][contains(.,'Sophia')]");
myname3 = browser.find_element_by_xpath("//option[@data-id='3'][contains(.,'Alice')]");
myname4 = browser.find_element_by_xpath("//option[@data-id='4'][contains(.,'Isabella')]");
myname5 = browser.find_element_by_xpath("//option[@data-id='5'][contains(.,'Manuela')]");
myname6 = browser.find_element_by_xpath("//option[@data-id='6'][contains(.,'Laura')]");
myname7 = browser.find_element_by_xpath("//option[@data-id='7'][contains(.,'Luiza')]");
myname8 = browser.find_element_by_xpath("//option[@data-id='8'][contains(.,'Valentina')]");
myname9 = browser.find_element_by_xpath("//option[@data-id='9'][contains(.,'Giovanna')]");
myname10 = browser.find_element_by_xpath("//option[@data-id='10'][contains(.,'Maria Eduarda')]");
myname11 = browser.find_element_by_xpath("//option[@data-id='11'][contains(.,'Helena')]");
myname12 = browser.find_element_by_xpath("//option[@data-id='12'][contains(.,'Beatriz')]");
myname13 = browser.find_element_by_xpath("//option[@data-id='13'][contains(.,'Maria Luiza')]");
myname14 = browser.find_element_by_xpath("//option[@data-id='14'][contains(.,'Lara')]");
myname15 = browser.find_element_by_xpath("//option[@data-id='15'][contains(.,'Julia')]");

myleftbox = browser.find_element_by_xpath("//select[contains(@class,'form-control pickListSelect pickData')]");
myrightbox = browser.find_element_by_xpath("//select[contains(@class,'form-control pickListSelect pickListResult')]");

addbutton = browser.find_element_by_xpath("//button[@class='pAdd btn btn-primary btn-sm'][contains(.,'Add')]");
addallbutton = browser.find_element_by_xpath("//button[@class='pAddAll btn btn-primary btn-sm'][contains(.,'Add All')]");
removebutton = browser.find_element_by_xpath("//button[@class='pRemove btn btn-primary btn-sm'][contains(.,'Remove')]");
removeallbutton = browser.find_element_by_xpath("//button[@class='pRemoveAll btn btn-primary btn-sm'][contains(.,'Remove All')]");

myname1.click();
time.sleep(mysecs);
myname2.click();
time.sleep(mysecs);
myname3.click();
time.sleep(mysecs);
addbutton.click();
time.sleep(mysecs);
myname10.click();
time.sleep(mysecs);
myname11.click();
time.sleep(mysecs);
myname12.click();
time.sleep(mysecs);
addbutton.click();
time.sleep(mysecs);

mynamer1 = browser.find_element_by_xpath("//option[@data-id='1'][contains(.,'Isis')]");
mynamer2 = browser.find_element_by_xpath("//option[@data-id='2'][contains(.,'Sophia')]");
mynamer3 = browser.find_element_by_xpath("//option[@data-id='3'][contains(.,'Alice')]");
mynamer4 = browser.find_element_by_xpath("//option[@data-id='10'][contains(.,'Maria Eduarda')]");
mynamer5 = browser.find_element_by_xpath("//option[@data-id='11'][contains(.,'Helena')]");
mynamer6 = browser.find_element_by_xpath("//option[@data-id='12'][contains(.,'Beatriz')]");

time.sleep(mysecs);
mynamer1.click();
time.sleep(mysecs);
mynamer2.click();
time.sleep(mysecs);
mynamer3.click();
time.sleep(mysecs);
mynamer4.click();
time.sleep(mysecs);
mynamer5.click();
time.sleep(mysecs);
mynamer6.click();
time.sleep(mysecs);
removebutton.click();
time.sleep(mysecs);
addallbutton.click();
time.sleep(mysecs);
removeallbutton.click();

#Open Data List Filter screen

InputForms26 = browser.find_element_by_link_text("List Box");
InputForms26.send_keys(Keys.DOWN);
browser.find_element_by_link_text("Data List Filter").send_keys(Keys.ENTER);

n1name = "bre";
n2email = "test3";
n3phone = "555";

searchlist = browser.find_element_by_xpath("//input[contains(@type,'search')]");
searchlist.send_keys(n1name);
time.sleep(mysecs);
searchlist.clear();
searchlist.send_keys(Keys.ENTER);
time.sleep(mysecs);
searchlist.send_keys(n2email);
time.sleep(mysecs);
searchlist.clear();
time.sleep(mysecs);
searchlist.send_keys(n3phone);
time.sleep(mysecs);
searchlist.clear();
searchlist.send_keys(Keys.ENTER);
time.sleep(mysecs);

workbook = xlsxwriter.Workbook('TestResults.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'TestResults')
worksheet.write('A3', 'Screen Name')
worksheet.write('B3', 'Variable Name')
worksheet.write('C3', 'Expected')
worksheet.write('D3', 'Actual')
worksheet.write('A4', 'Simple Form Demo')
worksheet.write('B4', 'input1')
worksheet.write('C4', input1)
worksheet.write('D4', a1)
worksheet.write('A5', 'Simple Form Demo')
worksheet.write('B5', 'msum1')
worksheet.write('C5', msum1)
worksheet.write('D5', a2)
worksheet.write('A6', 'Checkbox Demo')
worksheet.write('B6', 'input3')
worksheet.write('C6', input3)
worksheet.write('D6', a3)
worksheet.write('A7', 'Radio Buttons Demo')
worksheet.write('B7', 'out1')
worksheet.write('C7', out1)
worksheet.write('D7', a5)
worksheet.write('A8', 'Radio Buttons Demo')
worksheet.write('B8', 'out2')
worksheet.write('C8', out2)
worksheet.write('D8', a6)
worksheet.write('A9', 'Select Dropdown List')
worksheet.write('B9', 'expm1')
worksheet.write('C9', expm1)
worksheet.write('D9', a7)
worksheet.write('A10', 'Input Form Submit')
worksheet.write('B10', '')
worksheet.write('C10', '')
worksheet.write('D10', '')
worksheet.write('A11', 'Ajax Form Submit')
worksheet.write('B11', 'expsubmittext')
worksheet.write('C11', expsubmittext)
worksheet.write('D11', a8)
worksheet.write('A12', 'JQuery Select dropdown')
worksheet.write('B12', '')
worksheet.write('C12', '')
worksheet.write('D12', '')
worksheet.write('A13', 'Bootstrap Date Picker')
worksheet.write('B13', '')
worksheet.write('C13', '')
worksheet.write('D13', '')
worksheet.write('A14', 'Table Data Search')
worksheet.write('B14', 'mytest1')
worksheet.write('C14', mytest1)
worksheet.write('D14', a11)
worksheet.write('A15', 'Table Data Search')
worksheet.write('B15', 'mytest2')
worksheet.write('C15', mytest2)
worksheet.write('D15', a12)
worksheet.write('A16', 'Table Data Search')
worksheet.write('B16', 'mytest3')
worksheet.write('C16', mytest3)
worksheet.write('D16', a13)
worksheet.write('A17', 'Table Data Search')
worksheet.write('B17', 'mytest4')
worksheet.write('C17', mytest4)
worksheet.write('D17', a14)
worksheet.write('A18', 'Table Data Search')
worksheet.write('B18', 'mytest5')
worksheet.write('C18', mytest5)
worksheet.write('D18', a15)
worksheet.write('A19', 'Table Data Search')
worksheet.write('B19', 'mytest6')
worksheet.write('C19', mytest6)
worksheet.write('D19', a16)
worksheet.write('A20', 'Table Data Search')
worksheet.write('B20', 'mytest7')
worksheet.write('C20', mytest7)
worksheet.write('D20', a17)
worksheet.write('A21', 'Table Filter')
worksheet.write('B21', '')
worksheet.write('C21', '')
worksheet.write('D21', '')
worksheet.write('A22', 'Table Sort & Search')
worksheet.write('B22', 'mymessage1')
worksheet.write('C22', mymessage1)
worksheet.write('D22', a18)
worksheet.write('A23', 'Table Sort & Search')
worksheet.write('B23', 'mymessage2')
worksheet.write('C23', mymessage2)
worksheet.write('D23', a19)
worksheet.write('A24', 'Table Sort & Search')
worksheet.write('B24', 'mymessage3')
worksheet.write('C24', mymessage3)
worksheet.write('D24', a20)
worksheet.write('A25', 'Bootstrap Alerts')
worksheet.write('B25', 'm1')
worksheet.write('C25', m1)
worksheet.write('D25', a21)
worksheet.write('A26', 'Bootstrap Alerts')
worksheet.write('B26', 'm2')
worksheet.write('C26', m2)
worksheet.write('D26', a22)
worksheet.write('A27', 'Bootstrap Alerts')
worksheet.write('B27', 'm3')
worksheet.write('C27', m3)
worksheet.write('D27', a23)
worksheet.write('A28', 'Bootstrap Alerts')
worksheet.write('B28', 'm4')
worksheet.write('C28', m4)
worksheet.write('D28', a24)
worksheet.write('A29', 'Bootstrap Alerts')
worksheet.write('B29', 'm5')
worksheet.write('C29', m5)
worksheet.write('D29', a25)
worksheet.write('A30', 'Bootstrap Alerts')
worksheet.write('B30', 'm6')
worksheet.write('C30', m6)
worksheet.write('D30', a26)
worksheet.write('A31', 'Bootstrap Alerts')
worksheet.write('B31', 'm7')
worksheet.write('C31', m7)
worksheet.write('D31', a27)
worksheet.write('A32', 'Bootstrap Alerts')
worksheet.write('B32', 'm8')
worksheet.write('C32', m8)
worksheet.write('D32', a28)
worksheet.write('A33', 'Bootstrap Modals')
worksheet.write('B33', '')
worksheet.write('C33', '')
worksheet.write('D33', '')
worksheet.write('A34', 'Window Popup Modal')
worksheet.write('B34', '')
worksheet.write('C34', '')
worksheet.write('D34', '')
worksheet.write('A35', 'Progress Bar Modal')
worksheet.write('B35', '')
worksheet.write('C35', '')
worksheet.write('D35', '')
worksheet.write('A36', 'Javascript Alerts')
worksheet.write('B36', 'm11')
worksheet.write('C36', m11)
worksheet.write('D36', a29)
worksheet.write('A37', 'Javascript Alerts')
worksheet.write('B37', 'm12')
worksheet.write('C37', m12)
worksheet.write('D37', a30)
worksheet.write('A38', 'Javascript Alerts')
worksheet.write('B38', 'm15')
worksheet.write('C38', m15)
worksheet.write('D38', a31)
worksheet.write('A39', 'File Download')
worksheet.write('B39', '')
worksheet.write('C39', '')
worksheet.write('D39', '')
worksheet.write('A40', 'JQuery List Box')
worksheet.write('B40', '')
worksheet.write('C40', '')
worksheet.write('D40', '')
worksheet.write('A41', 'Data List Filter')
worksheet.write('B41', '')
worksheet.write('C41', '')
worksheet.write('D41', '')
workbook.close()

browser.quit();
