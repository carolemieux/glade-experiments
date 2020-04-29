package glade.constants.program;

import glade.constants.Files;
import glade.main.ProgramDataUtils.MultiFileProgramExamples;
import glade.main.ProgramDataUtils.ProgramData;
import glade.main.ProgramDataUtils.ProgramExamples;
import glade.main.ProgramDataUtils.ShellProgramData;
import glade.util.OracleUtils.IdentityWrapper;

public class ArithData {
    public static final String ARITH_EXE = "arith/parse_arith.py";
    public static final boolean ARITH_IS_ERROR = true;
    public static final String ARITH_EXTENSION = ".arith";
    public static final String ARITH_EMPTY = "1";

    public static final String ARITH_NAME = "arith";
    public static final ProgramData ARITH_DATA = new ShellProgramData(Files.FILE_PARAMETERS, ARITH_EXE, ARITH_IS_ERROR);
    public static final ProgramExamples ARITH_EXAMPLES = new MultiFileProgramExamples(Files.FILE_PARAMETERS, ARITH_NAME, ARITH_EXTENSION, ARITH_EMPTY, new IdentityWrapper());
}
