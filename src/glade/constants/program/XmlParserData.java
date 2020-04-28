package glade.constants.program;

import glade.constants.Files;
import glade.main.ProgramDataUtils.MultiFileProgramExamples;
import glade.main.ProgramDataUtils.ProgramData;
import glade.main.ProgramDataUtils.ProgramExamples;
import glade.main.ProgramDataUtils.ShellProgramData;
import glade.util.OracleUtils.IdentityWrapper;

public class XmlParserData {
    public static final String XML_EXE = "xml-parser/parse_xml";
    public static final boolean XML_IS_ERROR = true;
    public static final String XML_EXTENSION = ".xml";
    public static final String XML_EMPTY = "<a></a>";

    public static final String XML_NAME = "xml-parser";
    public static final ProgramData XML_DATA = new ShellProgramData(Files.FILE_PARAMETERS, XML_EXE, XML_IS_ERROR);
    public static final ProgramExamples XML_EXAMPLES = new MultiFileProgramExamples(Files.FILE_PARAMETERS, XML_NAME, XML_EXTENSION, XML_EMPTY, new IdentityWrapper());
}
