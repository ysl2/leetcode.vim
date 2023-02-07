import unittest
import os
import sys

plugin_dir = os.getcwd()
thirdparty_dir = os.path.join(plugin_dir, 'thirdparty')
if plugin_dir not in sys.path:
    sys.path.append(plugin_dir)
if thirdparty_dir not in sys.path:
    sys.path.append(thirdparty_dir)

os.environ['LEETCODE_BASE_URL'] = 'https://leetcode.com'
import leetcode
try:
    import keyring
    has_keyring = False
except ImportError:
    has_keyring = False

class TestLeetcode(unittest.TestCase):

    def setUp(self):
        leetcode.enable_logging()
        is_login = leetcode.signin("fake", "fake")
        self.assertEqual(is_login, True)

    def testGetProbles(self):
        leetcode.get_problems(["all"])


    def test_eqal(self):
        html='''
	<div id="list-card-app">
	  <span class="text-300 text-lg sidebar-title">
	    <i class="glyphicon glyphicon-fire" aria-hidden="true"></i>&nbsp; Top Hits</span>
	  <div class="list-group-item visible-sm visible-xs active">
	    <a href="/problemset/all/" class="text-gray text-400">
	      <div class="list-content-wrapper">
		<div class="pull-right"></div>All Problems</div>
	    </a>
	  </div>
	  <div class="list-group-item undefined ">
	    <a href="/problemset/top-100-liked-questions/" class="text-gray text-400">
	      <div class="list-content-wrapper">
		<div class="pull-right"></div>
		<span>
		  <i class="fa fa-list-ul fav-list-icon" aria-hidden="true"></i>&nbsp; Top 100 Liked Questions</span>
	      </div>
	    </a>
	  </div>
	  <div class="list-group-item undefined ">
	    <a href="/problemset/top-amazon-questions/" class="text-gray text-400">
	      <div class="list-content-wrapper">
		<div class="pull-right">
		  <i class="fa fa-lock"></i>
		</div>
		<span>
		  <i class="fa fa-list-ul fav-list-icon" aria-hidden="true"></i>&nbsp; Top Amazon Questions</span>
	      </div>
	    </a>
	  </div>
	  <div class="list-group-item undefined ">
	    <a href="/problemset/top-facebook-questions/" class="text-gray text-400">
	      <div class="list-content-wrapper">
		<div class="pull-right">
		  <i class="fa fa-lock"></i>
		</div>
		<span>
		  <i class="fa fa-list-ul fav-list-icon" aria-hidden="true"></i>&nbsp; Top Facebook Questions</span>
	      </div>
	    </a>
	  </div>
	  <div class="list-group-item undefined ">
	    <a href="/problemset/top-google-questions/" class="text-gray text-400">
	      <div class="list-content-wrapper">
		<div class="pull-right">
		  <i class="fa fa-lock"></i>
		</div>
		<span>
		  <i class="fa fa-list-ul fav-list-icon" aria-hidden="true"></i>&nbsp; Top Google Questions</span>
	      </div>
	    </a>
	  </div>
	  <div class="list-group-item undefined ">
	    <a href="/problemset/top-interview-questions/" class="text-gray text-400">
	      <div class="list-content-wrapper">
		<div class="pull-right"></div>
		<span>
		  <i class="fa fa-list-ul fav-list-icon" aria-hidden="true"></i>&nbsp; Top Interview Questions</span>
	      </div>
	    </a>
	  </div>
	  <div class="list-group-item undefined ">
	    <a href="/problemset/top-linkedin-questions/" class="text-gray text-400">
	      <div class="list-content-wrapper">
		<div class="pull-right">
		  <i class="fa fa-lock"></i>
		</div>
		<span>
		  <i class="fa fa-list-ul fav-list-icon" aria-hidden="true"></i>&nbsp; Top LinkedIn Questions</span>
	      </div>
	    </a>
	  </div>
	  <hr class="line dotted fav-list-hr hidden-xs hidden-sm">
	  <div class="list-group-item  ">
	    <a href="/contribute/" class="text-gray text-400">
	      <div class="list-content-wrapper">
		<div class="pull-right"></div>
		<span>
		  <i class="glyphicon glyphicon-heart contribute-icon" aria-hidden="true"></i>&nbsp; Contribute Question</span>
	      </div>
	    </a>
	  </div>
	</div>'''
        from bs4 import BeautifulSoup
        soup = BeautifulSoup(html, 'lxml')
        for li in soup.select('#list-card-app .undefined span'):
            print(li.get_text())


if __name__ == "__main__":
    unittest.main()
