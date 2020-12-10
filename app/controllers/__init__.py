from bottle import app

from .about import about_controller
from .author import author_controller
from .authors import authors_controller
from .browse import browse_controller
from .channels_and_repositories import channels_and_repositories_controller
from .code import code_controller
from .creating_package_files import creating_package_files_controller
from .customizing_packages import customizing_packages_controller
from .dependencies import dependencies_controller
from .developers import developers_controller
from .docs import docs_controller
from .events import events_controller
from .fetch import fetch_controller
from .five_hundred import five_hundred_controller
from .four_oh_four import four_oh_four_controller
from .index import index_controller
from .installation import installation_controller
from .issues import issues_controller
from .label import label_controller
from .labels import labels_controller
from .messaging import messaging_controller
from .new import new_controller
from .news import news_controller
from .opensearch_suggestions import opensearch_suggestions_controller
from .package import package_controller
from .packages import packages_controller
from .popular import popular_controller
from .refresh_package import refresh_package_controller
from .renaming_a_package import renaming_a_package_controller
from .rss import rss_controller
from .say_thanks import say_thanks_controller
from .search import search_controller
from .settings import settings_controller
from .stats import stats_controller
from .styles import styles_controller
from .submit import submit_controller
from .submitting_a_package import submitting_a_package_controller
from .syncing import syncing_controller
from .test_pr import test_pr_controller
from .test_repo import test_repo_controller
from .trending import trending_controller
from .troubleshooting import troubleshooting_controller
from .updated import updated_controller
from .usage import usage_controller
