const vscode = require('vscode');
const spawn = require('child_process').spawn;
const path = require('path')
const clipboardy = require("clipboardy");

/**
 * @param {vscode.ExtensionContext} context
 */
function activate(context) {
	
	let disposable = vscode.commands.registerCommand('annotation-translator.translate', async function () {

		const editor = vscode.window.activeTextEditor;
		const text = editor.document.getText()
		const result = spawn('python', [path.join(__dirname, 'model/func.py'), text]); // 파일 경로 받아오기 => __dirname

		result.stdout.on('data', async (data)=>{
			const articles = eval("("+data.toString()+")");
			const chkbox = [];
			for(var i in articles){
				const article = {
					label: articles[i]['detail'],
					detail: articles[i]['label']
				}

				chkbox[i] = article;
			}

			const article = await vscode.window.showQuickPick(chkbox, {
				matchOnDetail: true
			})
			if (article == null) return

			clipboardy.write(article.label)
		})

		result.stderr.on('data', function(data){
			console.log(data.toString());
		})

	});

	context.subscriptions.push(disposable);
}

function deactivate() {}

module.exports = {
	activate,
	deactivate
}
