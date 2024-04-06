//今回はGAS（Google Apps Script）を用いてgooglesheetでAIと会話ができるようにプログラムを作成しました。
//事前準備としてOPENAI社の公式ページからAPIキーを取得してください。
//取得したAPIキーをGASのプロジェクトの設定→下にスクロールしてスクリプトプロパティに追加してください。
//プロパティは　API_KEY　に、値は事前準備で取得したAPIキーを入力してください。
// let promptCell = sheetPrompt.getRange("W1");はどのセルでユーザーから入力を受けるか設定するコードです。
//A1やZ54などお好きなセルを指定してください。
//その他シート名やsystemPrompt = 'あなたはユーザーとフレンドリーに会話してください。なども変更が可能です。
//自分なりのAIで存分に会話を楽しみましょう！



function chatGptRequest() {
  // OpenAIのAPIキーを取得
  const apiKey = PropertiesService.getScriptProperties().getProperty('API_KEY');

  // OpenAIのエンドポイント
  const apiUrl = 'https://api.openai.com/v1/chat/completions';
  // System パラメータ
  const systemPrompt = 'あなたはユーザーとフレンドリーに会話してください。'
  // 入出力シート
  const sheetPrompt = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('sheet1');
  // 履歴シート
  const sheetHistory = SpreadsheetApp.getActiveSpreadsheet().getSheetByName('sheet2'); 
  // 履歴取得回数
  // token数の制限に引っかかるのであまり多くしないこと
  const historyNum = 1

  // 送信メッセージを定義
  let messages = [{'role': 'system', 'content': systemPrompt},];

  // 履歴シートから過去のやり取りを取得
  let history = sheetHistory.getRange(1,1,2,historyNum).getValues();

  // 過去の履歴を送信メッセージに追加する
  for (let i in history.reverse()){
    // 過去の履歴が空欄ではない場合は追加する
    if (history[i][0] && history[i][1]){
      // ユーザの質問
      messages.push({'role': 'user', 'content': history[i][0]});
      // ChatGPTのAPIレスポンス
      messages.push({'role': 'assistant', 'content': history[i][1]});
    }
  }

  // 入出力シートからの入力情報を取得
  let promptCell = sheetPrompt.getRange("W1");
  let prompt = promptCell.getValue();

  // 質問内容を追加
  messages.push({'role': 'user', 'content': prompt});

  // パラメータ設定
  const requestBody = {
    'model': 'gpt-3.5-turbo',
    'temperature': 0.7,
    'max_tokens': 4096,
    'messages': messages
  }

  // 送信内容を設定
  const request = {
    method: "POST",
    muteHttpExceptions : true,
    headers: {
      'Content-Type': 'application/json',
      'Authorization': 'Bearer ' + apiKey,
    },
    payload: JSON.stringify(requestBody),
  }

  // 回答先のセルを指定
  responseCell = sheetPrompt.getRange("X1");
  try {
    //OpenAIのChatGPTにAPIリクエストを送り、結果を変数に格納
    const response = JSON.parse(UrlFetchApp.fetch(apiUrl, request).getContentText());
    // ChatGPTのAPIレスポンスをセルに記載
    if (response.choices) {
      responseCell.setValue(response.choices[0].message.content);
      // 履歴シートの先頭に行を追加する
      sheetHistory.insertRowsBefore(1,1);
      // 今回のプロンプトの結果を履歴シートにコピー
      sheetPrompt.getRange(1,1,1,2).copyTo(sheetHistory.getRange(1,1,1,2));
    } else {
      // レスポンスが正常に返ってこなかった場合の処理
      console.log(response);
      responseCell.setValue(response);
    }
  } catch(e) {
    // 例外エラー処理
    console.log(e);
    responseCell.setValue(e);
  }
}