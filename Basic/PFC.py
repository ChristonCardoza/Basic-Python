import os
import sys
import shutil
import logging
import filecmp
import zipfile
import xml.etree.ElementTree as ET


class ParserFunctionsChecker:
    def __init__(self):
        """
        Constructor

        """
        self.PARENT_ROOT = os.getcwd()
        self.input_dir = "%s/input" % self.PARENT_ROOT
        self.output_dir = "%s/output" % self.PARENT_ROOT
        self.old_parsers = "%s/OldParsers" % self.input_dir
        self.cleaned_parsers = "%s/CleanedParsers" % self.input_dir

        log_filename = 'ParserFunctionsChecker.log'
        try:
            os.remove("ParserFunctionsChecker.log")
        except OSError:
            pass
        logging.basicConfig(filename=log_filename, level=logging.INFO,
                            format='%(asctime)s %(levelname)-8s %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S', filemode='w')
        logging.info("PARENT_ROOT : %s" % self.PARENT_ROOT)

        logging.info("Clearing output Directory")
        for root, dirs, files in os.walk(os.path.join(self.output_dir)):
            logging.info("Removing all the files from output directory: %s" % files)
            for file in files:
                os.remove(os.path.join(self.output_dir, file))
            for dir in dirs:
                shutil.rmtree(os.path.join(self.output_dir, dir))

        self.results_html = ReportEngine()
        self.create_html_report()

        #   Extraction of parser envision files in the Old Parsers folder
        self.file_list = os.listdir(self.old_parsers)
        for filename in self.file_list:
            zip_ref = zipfile.ZipFile(os.path.join(self.old_parsers, filename))
            zip_ref.extractall(self.old_parsers)
            zip_ref.close()
        # Working through each parser unzipped folder
        parser_folders = os.listdir(os.path.join(self.old_parsers, 'etc', 'devices'))
        for parser in parser_folders:
            self.parser = parser
            list_dir = os.listdir(os.path.join(self.old_parsers, 'etc', 'devices', parser))
            for files in list_dir:
                if files.endswith(".ini"):
                    continue
                elif files.endswith(".xml"):
                    #   Creating a file with count of functions in the parsers before Cleanup
                    with open('%s/OLD_Functions_Counter.txt' % self.output_dir, 'a') as outfile:
                        parser_file = open(os.path.join(self.old_parsers, 'etc', 'devices', parser, files),
                                           'r')
                        self.xml_contents = parser_file.read()
                        parser_file.close()
                        old_functions_count = self.xml_contents.count("&lt;@")
                        outfile.write("%s:%s\n" % (self.parser, old_functions_count))
                    outfile.close()

        #   Extraction of parser envision files in the Cleaned Parsers folder
        self.file_list = os.listdir(self.cleaned_parsers)
        for filename in self.file_list:
            zip_ref = zipfile.ZipFile(os.path.join(self.cleaned_parsers, filename))
            zip_ref.extractall(self.cleaned_parsers)
            zip_ref.close()
        # Working through each parser unzipped folder
        parser_folders = os.listdir(os.path.join(self.cleaned_parsers, 'etc', 'devices'))
        for parser in parser_folders:
            self.parser = parser
            list_dir = os.listdir(os.path.join(self.cleaned_parsers, 'etc', 'devices', parser))
            for files in list_dir:
                if files.endswith(".ini"):
                    continue
                elif files.endswith(".xml"):
                    #   Creating a file with count of functions in the parsers after Cleanup
                    #   followed with the check for duplicates in each function line in the parser after the cleanup
                    with open('%s/NEW_Functions_Counter.txt' % self.output_dir, 'a') as outfile:
                        parser_file = open(os.path.join(self.cleaned_parsers, 'etc', 'devices', parser, files),
                                           'r')
                        self.xml_contents = parser_file.read()
                        parser_file.close()
                        new_functions_count = self.xml_contents.count("&lt;@")
                        outfile.write("%s:%s\n" % (self.parser, new_functions_count))
                        self.parser_xml_tree = ET.parse(os.path.join(self.cleaned_parsers, 'etc', 'devices', parser,
                                                                     files))
                        self.parser_xml_root = self.parser_xml_tree.getroot()
                        for message_tag in self.parser_xml_root.findall('MESSAGE'):
                            if message_tag.get('functions'):
                                func_list = (message_tag.get('functions')).split('<@')
                                if len(func_list) == len(set(func_list)):
                                    pass
                                else:
                                    with open('%s/%s_FunctionDuplicatesResults.txt' % (self.output_dir, self.parser), 'a') as file:
                                        file.write(message_tag.get('id1'))
                                        file.write('\n')
                                        file.close()
                            else:
                                pass
                    outfile.close()
        self.file_list = os.listdir(self.output_dir)
        with open('%s/OLD_Functions_Counter.txt' % self.output_dir, 'r') as file_old, \
                open('%s/NEW_Functions_Counter.txt' % self.output_dir, 'r') as file_new:
            for old, new in zip(file_old, file_new):
                old = old.strip()
                new = new.strip()
                self.results_html.writeLine('<tr><td>%s</td><td>%s</td><td>%s</td>'
                                            % (old.split(':')[0], (old.split(':')[1]), new.split(':')[1]))
                if '%s_FunctionDuplicatesResults.txt' % (old.split(':')[0]) in self.file_list:
                    self.results_html.writeLine('<td style="text-align:center"><h3>'
                                                '<a href="%s/%s_FunctionDuplicatesResults.txt">'
                                                '<font color="red">YES</font></a></h3></td></tr>'
                                                % (self.output_dir, old.split(':')[0]))
                else:
                    self.results_html.writeLine('<td style="text-align:center"><h3><font color="green">NO</font>'
                                                '</h3></td></tr>')

        #   Compare the Functions count between the 2 files
        if not filecmp.cmp('%s/OLD_Functions_Counter.txt' % self.output_dir,
                           '%s/NEW_Functions_Counter.txt' % self.output_dir):
            f1 = open('%s/OLD_Functions_Counter.txt' % self.output_dir, 'r')
            f2 = open('%s/NEW_Functions_Counter.txt' % self.output_dir, 'r')
            OLD = f1.readlines()
            NEW = f2.readlines()
            f1.close()
            f2.close()
            with open('%s/Functions_Counter_Results.txt' % self.output_dir, 'a') as outfile:
                x = 0
                for i in OLD:
                    if i != NEW[x]:
                        outfile.writelines('OLD => %sNEW => %s' % (OLD[x], NEW[x]))
                        outfile.write('\n')
                    x += 1
            outfile.close()
        self.cleanup()

    def create_html_report(self):

        self.results_html.setFileName('%s/%s.html' % (self.output_dir, "ParserFunctionsCheck"))
        self.results_html.writeLine('<BR><BR><BR><table border="1" align="center">')
        self.results_html.writeLine('<tr bgcolor=#808080><th rowspan=2><h2>Parser Name</h2></th><th colspan=2>'
                                    '<h2>Functions Count</h2></th><th rowspan=2><h2>'
                                    'Duplicates present After Modification</h2></th></tr>')
        self.results_html.writeLine('<tr bgcolor=#808080><td><h2>Before Modification</h2></td>'
                                    '<td><h2>After Modification</h2></td></tr>')

    def cleanup(self):
        """

        :return:
        """

        print("Test Execution Complete...")
        sys.exit(0)


class ReportEngine(object):
    def __init__(self):
        pass

    def setFileName(self, file_name):
        self.fn = file_name
        self.writeHeadHtml()

    def writeLine(self, line):
        with open(self.fn, 'a') as f:
            f.write('%s\n' % line)

    def writeHeadHtml(self):
        with open(self.fn, 'w') as f:
            f.write("""\
    <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
        "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1" />
        <meta http-equiv="Content-Language" content="en" />
        <style type="text/css">
            body {
                background-color:  #ffffff;
                color: #000000;
                font:normal 68% verdana,arial,helvetica;
                font-size: 14px;
                padding-left: 0px;
                padding-top: 5px;
            }
            .header img {
              float: left;
              width: 120px;
              height: 100px;
            }
            .header {
              text-align: center;
              padding: 40px 0;
              font-size: 50px;
              font-weight:bold;
              position: relative;
            }
            h1 {
                font-size: 18px;
                background: #a6a6a6;
                margin-bottom: 0;
                padding-left: 5px;
                padding-top: 4px;
                padding-bottom: 4px;
                width: 100%;
            }
            h2 {
                font-size: 15px;
                color: #000000;
                text-align:center;
                padding-left: 5px;
                padding-top: 5px;
                padding-bottom: 5px;
                padding-right: 5px;
                width: 100%;
            }
            #status {
                font-family: "Trebuchet MS", Arial, Helvetica, sans-serif;
                border-collapse: collapse;
                width: 100%;
            }

            #status td, #status th {
                border: 1px solid grey;
                padding: 8px;
                text-align:center;
                vertical-align:middle;
            }

            #status td:hover {background-color: #ddd;}
            #status th {
                padding-top: 12px;
                padding-bottom: 12px;
                background-color: #0f4f14;
                color: white;
                text-align:center;
                vertical-align:middle;
            }
            .tooltip .tooltiptext {
                width: 120px;
                top: 100%;
                left: 50%;
                margin-left: -60px;
            }
            .tooltip {
                position: relative;
                display: inline-block;
                border-bottom: 1px dotted black;

            }
            .tooltip .tooltiptext {
                visibility: hidden;
                width: 450px;
                background-color: white;
                color: #fff;
                font-size: 13px;
                text-align: left;
                padding: 10px 10px;
                border-radius: 6px;
                position: absolute;
                z-index: 1;
                opacity: 0;
                transition: opacity 1s;
            }
            .tooltip:hover .tooltiptext {
                visibility: visible;
                opacity: 1;
            }
        </style>
    </head>
    <body>
    <div class="header">
      <img src="http://firstdistribution.com/wp-content/uploads/2016/08/Product-Page-NetWitness-Suite.png"alt="RSA Netwitness">
      Parser Functions Check Report
    </div>
    """)

    def writeClosingHtml(self):
        with open(self.fn, 'a') as f:
            f.write("""\
</body>
</html>
""")


"""
##############################################
                    main()
##############################################

"""
if __name__ == "__main__":
    ClassObj = ParserFunctionsChecker()





