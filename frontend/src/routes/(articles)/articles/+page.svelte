<script>
	import ArticleCard from './ArticleCard.svelte';
</script>

<div class="bg-white py-12">
	<div class="mx-auto max-w-7xl px-6 lg:px-8">
		<div class="mx-auto max-w-2xl lg:max-w-4xl">
			<h2 class="text-pretty text-4xl font-semibold tracking-tight text-primary sm:text-5xl">
				Recent news
			</h2>
			<p class="mt-2 text-lg text-muted">
				Discover the latest news, platform updates, expert tips, and guides
			</p>
			<div class="mt-16 space-y-20 lg:mt-20 lg:space-y-20">
				<ArticleCard />
				<ArticleCard />
			</div>
		</div>
	</div>
</div>
