import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import InlineKeyboardButton, CallbackQuery, InlineKeyboardMarkup, Message
from typing import Union
from pyrogram.types import InlineKeyboardButton
from MatrixMusic import app
from MatrixMusic.misc import HAPP, SUDOERS, XCB
from config import OWNER_ID
                                       
                                       
@app.on_callback_query(filters.regex("zzzback"))
async def zzzback(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
♡ مرحبا يزميلي
♡ استخدم الازرار بالاسفل
♡ ل- تصفح بوت ماكس
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "‹ اوامر التشغيل ›", callback_data="zzzll"),
                ],[
                    InlineKeyboardButton(
                        "‹ اوامر القناة ›", callback_data="zzzch"),
                    InlineKeyboardButton(
                        "‹ اوامر الادمن ›", callback_data="zzzad"),
                ],[
                    InlineKeyboardButton(
                        "‹ اوامر المطور ›", callback_data="zzzdv"),
                ],[
                    InlineKeyboardButton(
                        "‹ َٰ𝚂ُِ𝙾ِّ𝚄ٓ𝚁ٍّ𝙲ٍ𝙴 ٍ𝙴ٓ𝚁ٓ𝚁ُِ𝙾ٓ𝚁 ›", url="https://t.me/JOE_Ch")
                ],[
                   InlineKeyboardButton(
                      "مبرمج السورس", url="https://t.me/Y_O_JOE"
                   )
                ]
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzdv") & SUDOERS)
async def mpdtsf(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
♡ مرحبا يمعلم الاستاذ المطور
♡ الازرار اهي 
♡ انت فاهم بقي
       """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "التحديث", callback_data="zzzup"),
                ],[
                    InlineKeyboardButton(
                        "الرفع", callback_data="zzzsu"),
                    InlineKeyboardButton(
                        "الحظر", callback_data="zzzbn"),
                ],[
                    InlineKeyboardButton(
                        "اشعارات & المساعد", callback_data="zzzas"),
                ],[
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
                ],
            ]
        ),
    )



@app.on_callback_query(filters.regex("zzzll"))
async def zzzll(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
 ↯︙قائمــة اوامــر الـتشغـيـل ◍︙
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + (اسم الاغنية / رابط الاغنية)
</>- لـ تشغيل اغنية في المكالمة الصوتية</>

فيديو + (اسم المقطع / رابط المقطع)
</>- لـ تشغيل فيديو في المكالمة المرئية</>

بحث + الاسم
</>- لـ تحميل المقاطع الصوتيه من اليوتيوب</>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzad"))
async def zzzad(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
 ↯︙قائمة اوامر الادمن ◍︙
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
الاعدادات
 لـ عرض إعدادات اوضاع التشغيل</>

ايقاف / انهاء / اسكت
</>- لـ إيقاف تشغيل الموسيقى في المكالمة</>

وقف / توقف
</>- لـ إيقاف تشغيل الموسيقى في المكالمة مؤقتاً</>

كمل / كملي
</>- لـ إستئناف تشغيل الموسيقى في المكالمة</>

تخطي
<b>- لـ تخطي الاغنية وتشغيل الاغنية التاليه</b>

الاغاني
</>- لـ معرفة الاغاني الموجودة في قائمة الانتظار</>

بنج
</>- لـ عرض سرعة تشغيل البوت</>

رفع ادمن/تنزيل ادمن
</>- لـ رفع/تنزيل ادمن في البوت</>

الادمنيه
</>- لـ عرض قائمة ادمنية البوت</>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzch"))
async def zzzch(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙قائمة اوامر التشغيل في القناة ◍︙
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
<>- ارفع البوت إشراف في القناة و شغل مباشر</>
<>- ارسل (/channelplay او ربط) + يوزر القناة ل الربط</>
<>- ثم استخدم الاوامر بالاسفل ل التشغيل</>
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
تشغيل + اسم الاغنية
</>- لـ تشغيل اغنية في المكالمة الصوتية</>

فيديو + اسم المقطع
</>- لـ تشغيل فيديو في المكالمة المرئية</>

ايقاف / انهاء / اسكت
</>- لـ إيقاف تشغيل الموسيقى في المكالمة</>

وقف / توقف
</>- لـ إيقاف تشغيل الموسيقى في المكالمة مؤقتاً</>

كمل / استئناف
</>- لـ إستئناف تشغيل الموسيقى في المكالمة</>

تخطي
</>- لـ تخطي الاغنية وتشغيل الاغنية التاليه</>

/seek + عدد الثواني
</>- لـ تقديم الاغنيه ل الامام</>
/seekback + عدد الثواني
</>- لـ إرجاع الاغنيه ل الخلف</>
""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "رجوع", callback_data="zzzback"),
               ],
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzup") & SUDOERS)
async def zzzup(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙قائمة اوامر المطور ◍︙
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
 قائمة اوامر التحديثات :</>

السجلات
</>- لـ جلب سجلات البوت</>

تحديث
</>- لـ تحديث البوت</>

اعاده تشغيل
</>- لـ اعادة تشغيل البوت</>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                       "سورس", url="https://t.me/JOE_Ch"
                    )      ,
                    InlineKeyboardButton(
                       "المبرمج", url="https://t.me/Y_O_JOE"
                    )
                               
               ],[
                  InlineKeyboardButton(
                     "رجوع", callback_date="zzzdv"
                  )
               ],[
                  InlineKeyboardButton(
                     "رجوع الي البدايه", callback_date="zzzback"
                  )
               ]
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzsu") & SUDOERS)
async def zzzsu(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙قائمة اوامر المطور ◍︙
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
 قائمة اوامر الرفع </>

رفع مطور/تنزيل مطور
</>- ل رفع/تنزيل شخص مطور في ميوزك البوت</>

المطورين
</>- ل عرض قائمة مطورين البوت</>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                  InlineKeyboardButton(
                    "سورس", url="https://t.me/JOE_Ch"
                    ),
                    InlineKeyboardButton(
                       "المبرمج", url="https://t.me/Y_O_JOE"
                    )
               ],[
                  InlineKeyboardButton(
                    "رجوع", callback_data="zzzdv"
                  )
               ],[
                  InlineKeyboardButton(
                     "رجوع الي البدايه", callback_date="zzzback"
                  )
               ]
          ]
        ),
    )



@app.on_callback_query(filters.regex("zzzbn") & SUDOERS)
async def zzzbn(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯︙قائمة اوامر المطور ◍︙
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
قائمة اوامر الحظر :</>

بلوك/الغاء بلوك/المبلكين
</>- ل حظر/الغاء حظر شخص من استخدام ميوزك البوت</>

احظره عام/الغاء حظره عام
</>- ل حظر/الغاء حظر شخص من استخدام ميوزك البوت عام</>

المحظورين عام
</>- ل جلب قائمة المحظورين عام في البوت</>

حظر مجموعة/سماح
</>- ل حظر/الغاء حظر مجموعة من استخدام ميوزك البوت</>

المجموعات المحظورة
</>- ل جلب قائمة بالمجموعات المحظورة من استخدام البوت</>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                    InlineKeyboardButton(
                        "السورس", url="https://t.me/JOE_Ch"
                        ),
                    InlineKeyboardButton(
                       "المبرمج", url="https://t.me/Y_O_JOE"
                    )
               ],[
                  InlineKeyboardButton(
                     "رجوع", callback_data="zzzdv"
                  )
               ],[
                  InlineKeyboardButton(
                     "رجوع الي البدايه", callback_date="zzzback"
                  )
               ]
          ]
        ),
    )


@app.on_callback_query(filters.regex("zzzas") & SUDOERS)
async def zzzas(_, query: CallbackQuery):
   await query.edit_message_text(
       f"""
↯ ︙قائمة اوامر المطور ◍︙
ٴ⋆┄─┄─┄─┄─┄─┄─┄─┄⋆
قائمة اوامر المساعد :</>

السجل ⦗ تفعيل / تعطيل ⦘
</>- ل تفعيل/تعطيل اشعارات مجموعة سجل البوت</>

⦗ المغادره التلقائيه ⦗ تفعيل / تعطيل
</>- ل تفعيل/تعطيل المغادره التلقائيه ل الحساب المساعد من المجموعات عند عدم الاستخدام</>

""",
       reply_markup=InlineKeyboardMarkup(
          [
               [
                InlineKeyboardButton(
                        "‹ رجوع ›", callback_data="zzzdv"
                        ),
               ],[
                  InlineKeyboardButton(
                     "رجوع الي البدايه", callback_date="zzzback"
                  )
               ]
        ]
        ),
   )
