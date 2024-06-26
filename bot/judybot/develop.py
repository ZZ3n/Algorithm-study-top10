import discord
import os
import random
from discord.ext import commands
from dotenv import load_dotenv

# .env 파일에서 환경 변수를 로드
load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

if TOKEN is None:
    raise ValueError("DISCORD_TOKEN이 환경 변수로 설정되지 않았습니다.")

# 인텐트를 설정
intents = discord.Intents.default()
intents.message_content = True

# 봇 명령어 프리픽스 설정
bot = commands.Bot(command_prefix='/', intents=intents)

# 다양한 주제의 문장 리스트
sentences = [
    "바람이 방향을 바꾸면 우산은 춤을 출까요?",
    "과자는 왜 항상 끝이 아쉬울까요?",
    "전화기가 먼저 전화를 걸면 누구에게 걸까요?",
    "빨간색 사과와 초록색 사과가 싸우면 누가 이길까요?",
    "모든 고양이가 동시에 점프하면 지구가 흔들릴까요?",
    "새가 수영을 배운다면 어떤 스타일로 수영할까요?",
    "모든 꽃이 밤에만 핀다면 어떻게 될까요?",
    "물고기가 하늘을 날면 어떤 풍경일까요?",
    "바다 속에는 얼마나 많은 비밀이 숨어 있을까요?",
    "구름이 말을 한다면 어떤 이야기를 할까요?",
    "달에서 치즈를 먹으면 어떤 맛일까요?",
    "거북이가 집을 떠난다면 어디로 갈까요?",
    "무지개 끝에는 정말 보물이 있을까요?",
    "모든 나무가 이동할 수 있다면 어디로 갈까요?",
    "별이 밤에만 반짝이는 이유는 뭘까요?",
    "바람이 쉬면 무슨 소리를 낼까요?",
    "바닷물은 왜 짤까요?",
    "시간이 멈춘다면 우리는 알 수 있을까요?",
    "모든 강아지가 동시에 짖으면 어떤 소리가 날까요?",
    "피자는 왜 동그랄까요?",
    "고양이는 우주에서도 점프할 수 있을까요?",
    "거울 속의 나는 나를 보고 무슨 생각을 할까요?",
    "초콜릿이 녹지 않는다면 어떤 맛일까요?",
    "모든 벽이 이야기를 들려준다면 어떤 이야기를 할까요?",
    "우산이 비를 싫어한다면 어떻게 될까요?",
    "컴퓨터가 잠을 잘 수 있다면 어떤 꿈을 꿀까요?",
    "새가 말을 한다면 어떤 이야기를 할까요?",
    "꽃이 춤을 출 수 있다면 어떤 춤을 출까요?",
    "구두가 말을 한다면 무슨 이야기를 할까요?",
    "하늘이 녹색이라면 어떤 기분일까요?",
    "하늘에서 초콜릿이 내리면 모두 행복해질까요?",
    "기차가 날 수 있다면 어디로 갈까요?",
    "모든 나무가 춤을 출 수 있다면 어떤 춤을 출까요?",
    "거북이가 마라톤에 출전한다면 몇 시간을 걸릴까요?",
    "강아지가 주인을 산책시킨다면 어떤 일이 벌어질까요?",
    "고양이가 피자를 만든다면 어떤 맛일까요?",
    "자동차가 날 수 있다면 하늘은 교통 체증이 있을까요?",
    "별이 바다에 떠 있다면 물고기는 별을 잡을까요?",
    "바다가 사라진다면 세상은 어떻게 될까요?",
    "모든 집이 이동할 수 있다면 어디로 갈까요?",
    "오늘 하루도 반짝반짝 빛나는 날 되세요!",
    "당신의 웃음이 세상을 밝게 만듭니다.",
    "모든 일이 잘 풀리길 바랍니다.",
    "행운이 항상 당신 곁에 머물길!",
    "당신의 노력이 결실을 맺을 거예요.",
    "좋은 일이 가득하길 기원합니다.",
    "당신의 꿈이 이루어지길 바랍니다.",
    "매일 행복한 일이 가득하길!",
    "행운이 당신을 찾아올 거예요.",
    "모든 어려움이 순조롭게 해결되길 바랍니다.",
    "행복이 당신의 발걸음을 따라다닐 거예요.",
    "당신의 미소가 세상을 밝게 만들어요.",
    "오늘도 멋진 하루 되세요!",
    "당신의 열정이 성공을 이끌 것입니다.",
    "행운이 당신의 길을 밝게 비추길 바랍니다.",
    "당신의 인생에 기쁨과 행복이 가득하길 바랍니다.",
    "오늘도 좋은 일이 가득하길!",
    "당신의 웃음소리가 세상에 울려 퍼지길 바랍니다.",
    "모든 일이 잘 풀리길 바랍니다.",
    "당신의 하루가 무지개처럼 아름답길!",
    "행운이 당신의 손을 잡아주길 바랍니다.",
    "오늘도 좋은 소식이 있기를 바랍니다.",
    "당신의 마음이 항상 편안하길 바랍니다.",
    "모든 어려움이 순조롭게 해결되길 바랍니다.",
    "당신의 웃음소리가 세상에 울려 퍼지길 바랍니다.",
    "행운이 당신의 길을 환히 비추길 바랍니다.",
    "당신의 인생에 기쁨과 행복이 가득하길 바랍니다.",
    "오늘도 행운이 당신을 찾아오길 바랍니다.",
    "좋은 일만 가득하길 바랍니다.",
    "당신의 하루가 행복으로 가득하길 바랍니다.",
    "행복한 순간이 매일매일 이어지길!",
    "모든 꿈이 이루어질 거예요. 믿으세요!",
    "오늘도 활짝 웃는 얼굴로 시작해요!",
    "모든 일이 술술 잘 풀리길!",
    "당신의 노력이 결실을 맺을 거예요.",
    "모든 일이 순조롭게 풀리길 바랍니다.",
    "오늘도 행복한 하루 되세요!",
    "당신의 열정이 성공을 이끌 것입니다.",
    "당신의 꿈이 이루어지길 기원합니다.",
    "행운이 당신의 발걸음을 따라다닐 거예요.",
    "당신의 미소가 세상을 밝게 만들어요.",
    "모든 일이 잘 풀리길 바랍니다.",
    "좋은 일이 가득하길 기원합니다.",
    "당신의 꿈이 이루어지길 바랍니다.",
    "매일 행복한 일이 가득하길!",
    "행운이 당신을 찾아올 거예요.",
    "모든 어려움이 순조롭게 해결되길 바랍니다.",
    "행복이 당신의 발걸음을 따라다닐 거예요.",
    "당신의 미소가 세상을 밝게 만들어요.",
    "오늘도 멋진 하루 되세요!",
    "당신의 열정이 성공을 이끌 것입니다.",
    "행운이 당신의 길을 밝게 비추길 바랍니다.",
    "당신의 인생에 기쁨과 행복이 가득하길 바랍니다.",
    "오늘도 좋은 일이 가득하길!",
    "당신의 웃음소리가 세상에 울려 퍼지길 바랍니다.",
    "모든 일이 잘 풀리길 바랍니다.",
    "당신의 하루가 무지개처럼 아름답길!",
    "행운이 당신의 손을 잡아주길 바랍니다.",
    "오늘도 좋은 소식이 있기를 바랍니다.",
    "당신의 마음이 항상 편안하길 바랍니다."
]

@bot.event
async def on_ready():
    print(f'Logged on as {bot.user}!')
    await bot.change_presence(status=discord.Status.online, activity=discord.Game("대기중"))

@bot.command(name='주디')
async def send_random_sentence(ctx, channel_id: int):
    """지정된 채널에 랜덤한 문장을 보내는 명령어"""
    channel = bot.get_channel(channel_id)
    if channel is None:
        await ctx.send("지정된 채널을 찾을 수 없습니다.")
        return
    sentence = random.choice(sentences)
    await channel.send(sentence)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("해당 명령어를 찾을 수 없습니다.")
    else:
        await ctx.send(f"명령어 실행 중 오류가 발생했습니다: {error}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # 봇 자체의 메시지는 무시

    # on_message 이벤트에서도 명령어 처리기와 연동되도록 설정
    await bot.process_commands(message)

bot.run(TOKEN)
