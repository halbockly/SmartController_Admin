$(function(){
    $(".edit_btn").on("click", function(){
        // データ取得
        $(".mchn_id").text($(this).parent().prevAll(".dt_col_1").text());
        $(".ed_col_1").val($(this).parent().prevAll(".dt_col_1").text());
        $(".ed_col_2").val($(this).parent().prevAll(".dt_col_2").text());
        $(".ed_col_3").val($(this).parent().prevAll(".dt_col_3").text());

        // 編集フォーム表示
        $(".edit_box").addClass("open");
        $(".edit_box").removeClass("hide");
    });

    $(".cancel_btn").on("click", function(){
        // キャンセルボタン押下時、編集フォーム非表示
        $(".edit_box").addClass("hide");
        $(".edit_box").removeClass("open");
    });
});