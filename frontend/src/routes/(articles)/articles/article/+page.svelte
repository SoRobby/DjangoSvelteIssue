<script lang="ts">
	import { Button } from '$lib/components/ui/button';
</script>

<div
	class="relative h-[460px] w-full bg-[url('https://flowbite.s3.amazonaws.com/blocks/marketing-ui/articles/background.png')] bg-cover bg-center bg-no-repeat bg-blend-darken xl:h-[537px]"
>
	<div class="absolute left-0 top-0 h-full w-full bg-black bg-opacity-50"></div>
	<div
		class="absolute left-1/2 top-20 mx-auto w-full max-w-screen-xl -translate-x-1/2 px-4 xl:top-1/2 xl:-translate-y-1/2 xl:px-6"
	>

		<h1
			class="mb-4 max-w-4xl text-2xl font-extrabold leading-none text-white sm:text-3xl lg:text-4xl"
		>
			ArticleTitle
		</h1>
		
	</div>
</div>

<div class="relative z-10 mx-4 flex max-w-screen-xl justify-between gap-12 rounded bg-white p-6 xl:mx-auto xl:p-10"
>
	<article class="w-full max-w-none space-y-8">
		<div class="flex flex-col justify-between lg:flex-row lg:items-center">
			<div class="flex items-center gap-x-2 text-lg text-gray-500">
				<div>
					<span>By</span>
					<span class="font-semibold text-gray-800 hover:underline">AuthorName</span>
				</div>
			</div>
		</div>

		<div class="text-2xl text-muted">Article meta description...</div>
		<div class="space-y-4 pb-6 text-xl text-tertiary">
			<p>
				Litora consectetur risus nisl torquent neque non. Efficitur quis potenti dui taciti
				phasellus. Pharetra luctus porta dis netus penatibus accumsan. Orci varius aliquam varius
				montes curae sed. Per taciti etiam fames curabitur curae mus nec lorem curae. Non nisl justo
				nulla aenean interdum scelerisque at turpis. Congue iaculis lobortis nostra sociosqu tempus;
				eros mollis volutpat pellentesque.
			</p>

			<p>
				Fusce nullam at curae fusce risus. Efficitur nascetur enim nullam sapien scelerisque
				vulputate pellentesque erat aliquet. Mi mauris duis habitasse netus pretium sem. Pharetra
				sapien laoreet finibus venenatis litora fusce neque eu. Risus sociosqu diam orci senectus
				aliquam vitae sollicitudin vel class. Auctor in quam fames nisl non dapibus. Primis enim
				eros, auctor nec etiam sodales.
			</p>

			<p>
				Nam dignissim quis mus phasellus blandit lacinia egestas dolor montes. Fames vehicula velit
				class urna ridiculus; commodo torquent justo posuere. Conubia pulvinar mattis bibendum
				nascetur aenean litora blandit interdum. Natoque lacinia volutpat pretium phasellus
				pellentesque sapien efficitur. Nostra donec orci cursus morbi; per nisl integer. Lacinia
				auctor ex pulvinar taciti odio; nullam maximus egestas. Ultricies eros vivamus enim lacinia
				in vulputate litora condimentum pulvinar. Eleifend hac condimentum tortor rutrum ex? Ante
				primis pharetra maecenas, donec magnis faucibus? Dapibus aliquet aptent rutrum; turpis
				cursus consectetur.
			</p>

			<p>
				Volutpat sociosqu magna orci non rhoncus praesent; ridiculus tempor. Dictumst volutpat erat
				dictum posuere placerat ex arcu. Gravida aptent ultricies tempor sagittis urna interdum.
				Consequat leo fames duis at quis laoreet. Nostra praesent dolor efficitur; ut rutrum platea.
				Lorem cras vivamus mattis nunc orci erat augue. Diam est magnis lorem cursus tristique
				vehicula pretium inceptos adipiscing.
			</p>
		</div>
	</article>

	<aside class="hidden lg:block">
		<div class="w-96 space-y-12">
			<div>
				<h4 class="text-sm font-bold uppercase text-primary">News Headlines</h4>
				<p class="mt-2 text-sm text-muted">
					Get all the stories you need-to-know from the most powerful name in news delivered first
					thing every morning to your inbox.
				</p>
				<div class="mt-4">
					<Button size="sm" type="button" class="w-full">Subscribe</Button>
				</div>
			</div>
		</div>
	</aside>
</div>
