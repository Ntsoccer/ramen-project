# ramen-project
このブログアプリを作った理由：私自身よくラーメンを食べに行くが、少し遠くで食べておいしかったラーメンを記録しておきたい、また皆と美味しいラーメン店を共有したいという想いで作りました。
　　　　　　　　　　　　　　　またログインさえすれば誰でも投稿できるようにすることにより、皆が食べておいしかったラーメンを知り、共有しあえる、またコメントを誰でもすることが出来るようにすること                              で、感想を言い合える、そのようなラーメンコミュニティを作りたいと思い作成しました。
                      
                      
難しかった点、躓いた点：投稿詳細ページでコメントの表示させるさいpostのidが必要であった。
                      また同ページでその投稿が属しているカテゴリーと同じものを5件まで表示させる際、get_context_dataでカテゴリーの情報を取得する時、filterでcategory=detail_data.categoryと
                      するという点が苦戦した。
　　　　　　　　　　　　ログインしているユーザーのみのお気に入り一覧を表示させるために、ListView継承クラスにget_queryset関数内でreturnとしてuserのidを返す必要があった。
                      お問い合わせフォームでメール送信させるのに必要なsend_mail関数が、引数を必ず4つとることを知らず苦戦した。
            　　　　　
