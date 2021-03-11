// Copyright 2015-2016 Stanford University
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.

package glade.util;

public class OracleUtils {
	public interface Oracle {
		public String execute(String query);
		public int getCalls();
	}
	
	public interface DiscriminativeOracle {
		public abstract boolean query(String query);
		public int getCalls();
	}
	
	public static interface Wrapper {
		public abstract String wrap(String input);
	}
	
	public static class IdentityWrapper implements Wrapper {
		@Override
		public String wrap(String input) {
			return input;
		}
	}
	
	public static class WrappedOracle implements Oracle {
		private final Oracle oracle;
		private final Wrapper wrapper;
		private int numCalls = 0;
		
		public WrappedOracle(Oracle oracle, Wrapper wrapper) {
			this.oracle = oracle;
			this.wrapper = wrapper;
		}

		@Override
		public int getCalls() {
			return numCalls;
		}
		
		@Override
		public String execute(String query) {
			numCalls+= 1;
			return this.oracle.execute(this.wrapper.wrap(query));
		}
	}
	
    public static class WrappedDiscriminativeOracle implements DiscriminativeOracle {
        private final DiscriminativeOracle oracle;
        private final Wrapper wrapper;
        private int numCalls;

        public WrappedDiscriminativeOracle(DiscriminativeOracle oracle, Wrapper wrapper) {
                this.oracle = oracle;
                this.wrapper = wrapper;
        }

        @Override
        public boolean query(String query) {
        	numCalls += 1;
        	return this.oracle.query(this.wrapper.wrap(query));
        }

		@Override
		public int getCalls() {
        	return numCalls;
        }
    }
}
