package glade.constants.program;

import glade.constants.Files;
import glade.main.ProgramDataUtils.MultiFileProgramExamples;
import glade.main.ProgramDataUtils.ProgramData;
import glade.main.ProgramDataUtils.ProgramExamples;
import glade.main.ProgramDataUtils.ShellProgramData;
import glade.util.OracleUtils.IdentityWrapper;

public class WhilePyData {
    public static final String WHILEPY_EXE = "while/parse_whilepy.py";
    public static final boolean WHILEPY_IS_ERROR = true;
    public static final String WHILEPY_EXTENSION = ".py";
    public static final String WHILEPY_EMPTY = "passNEWLINE";

    public static final String WHILEPY_NAME = "whilepy";
    public static final ProgramData WHILEPY_DATA = new ShellProgramData(Files.FILE_PARAMETERS, WHILEPY_EXE, WHILEPY_IS_ERROR);
    public static final ProgramExamples WHILEPY_EXAMPLES = new MultiFileProgramExamples(Files.FILE_PARAMETERS, WHILEPY_NAME, WHILEPY_EXTENSION, WHILEPY_EMPTY, new IdentityWrapper());
}
