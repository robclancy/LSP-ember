from lsp_utils import NpmClientHandler
import os

def plugin_loaded():
	LspEmberPlugin.setup()

def plugin_unloaded():
	LspEmberPlugin.cleanup()

class LspEmberPlugin(NpmClientHandler):
	package_name = __package__
	server_directory = "server"
	server_binary_path = os.path.join(server_directory, "node_modules", "@lifeart", "ember-language-server", "bin", "ember-language-server.js")
