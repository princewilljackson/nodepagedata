from django.urls import path
from .views import *

urlpatterns = [
    path('bitpay/', BitPayViews.as_view()),
    path('solana/', SolanaViews.as_view()),
    path('trust/', TrustViews.as_view()),
    path('metamask/', MetamaskViews.as_view()),
    path('huobiwallet/', HuobiWalletViews.as_view()),
    path('phantom/', PhantomViews.as_view()),
    path('wazirx/', WazirxViews.as_view()),
    path('pillar/', PillarViews.as_view()),
    path('tokenpocket/', TokenpocketViews.as_view()),
    path('atomic/', AtomicViews.as_view()),
    path('walleth/', WallethViews.as_view()),
    path('authereum/', AuthereumViews.as_view()),
    path('eidoo/', EidooViews.as_view()),
    path('zelcore/', ZelcoreViews.as_view()),
    path('nash/', NashViews.as_view()),
    path('coinomi/', CoinomiViews.as_view()),
    path('gridplus/', GridplusViews.as_view()),
    path('coolwallets/', CoolWalletSViews.as_view()),
    path('alice/', AliceViews.as_view()),
    path('alphaWallet/', AlphaWalletViews.as_view()),
    path('tokenary/', TokenaryViews.as_view()),
    path('safepal/', SafepalViews.as_view()),
    path('equal/', EqualViews.as_view()),
    path('infinito/', InfinitoViews.as_view()),
    path('mathwallet/', MathwalletViews.as_view()),
    path('myKey/', MyKeyViews.as_view()),
    path('spatium/', SpatiumViews.as_view()),
    path('walletio/', WalletioViews.as_view()),
    path('infinitywallet/', InfinityWalletViews.as_view()),
    path('ownbit/', OwnBitViews.as_view()),
    path('easypocket/', EasyPocketViews.as_view()),
    path('onto/', ONTOViews.as_view()),
    path('bridgewallet/', BridgeWalletViews.as_view()),
    path('sparkpoint/', SparkPointViews.as_view()),
    path('viawallet/', ViaWalletViews.as_view()),
    path('coin98/', Coin98Views.as_view()),
    path('bitkeep/', BitKeepViews.as_view()),
    path('vision/', VisionViews.as_view()),
    path('sfwtwallet/', SFWTWalletViews.as_view()),
    path('peakdefi/', PeakDefiViews.as_view()),
    path('unstoppablewallet/', UnstoppableWalletViews.as_view()),
    path('meetone/', MEETONEViews.as_view()),
    path('dokwallet/', DOKWalletViews.as_view()),
    path('atwallet/', ATWalletViews.as_view()),
    path('morixwallet/', MoriXWalletViews.as_view()),
    path('midaswallet/', MidasWalletViews.as_view()),
    path('others/', OthersViews.as_view())
]
