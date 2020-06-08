package glade.constants.program;

import glade.constants.Files;
import glade.main.ProgramDataUtils.MultiFileProgramExamples;
import glade.main.ProgramDataUtils.ProgramData;
import glade.main.ProgramDataUtils.ProgramExamples;
import glade.main.ProgramDataUtils.ShellProgramData;
import glade.util.OracleUtils.IdentityWrapper;

public class WhileData {
    public static final String WHILE_EXE = "while/parse_while.py";
    public static final boolean WHILE_IS_ERROR = true;
    public static final String WHILE_EXTENSION = ".while";
    public static final String WHILE_EMPTY = "L=n";

    public static final String WHILE_NAME = "while";
    public static final ProgramData WHILE_DATA = new ShellProgramData(Files.FILE_PARAMETERS, WHILE_EXE, WHILE_IS_ERROR);
    public static final ProgramExamples WHILE_EXAMPLES = new MultiFileProgramExamples(Files.FILE_PARAMETERS, WHILE_NAME, WHILE_EXTENSION, WHILE_EMPTY, new IdentityWrapper());
}
